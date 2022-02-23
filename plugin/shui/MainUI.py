import os
import sys
from sys import argv
import json

from PyQt5 import (QtCore, QtWidgets)
from .utils import (ConnectionThread, Core, ConsoleTab, FileTab)
from PyQt5.QtNetwork import (QNetworkAccessManager, QNetworkProxy)


class App(QtCore.QObject):
    wifiUart=None
    config=None
    selectedPrinter = 0
    startMode = Core.StartMode.UNKNOWN
    outputFileName=None
    inputFileName=None

    onProgress = QtCore.pyqtSignal(object, object)
    onMessage = QtCore.pyqtSignal(object)
    onUploadFinished = QtCore.pyqtSignal(object)
    onUartRow = QtCore.pyqtSignal(object)
    onUartMessage = QtCore.pyqtSignal(object)
    onUartConnect = QtCore.pyqtSignal(object)

    def __init__(self, appStartMode):
        super().__init__()
        self.startMode=appStartMode
        if appStartMode== Core.StartMode.PRUSA:
            self.startMode = Core.StartMode.PRUSA
            self.outputFileName = str(os.getenv('SLIC3R_PP_OUTPUT_NAME'))
            self.inputFileName=sys.argv[1]
        elif appStartMode== Core.StartMode.STANDALONE:
            if len(argv)>1:
                self.inputFileName=sys.argv[1]
            else:
                if os.getenv('START_MODE')=='TEST':
                    self.inputFileName="/home/shubin/electronic/firmware/mks-robin/my/shui-src/bh.gcode"
            pass
        if self.inputFileName is not None and self.outputFileName is None:
            self.outputFileName = os.path.basename(self.inputFileName)
        self.wifiUart = ConnectionThread(self)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")) as jf:
            self.config=json.load(jf)
            jf.close()

        self.proxy=QNetworkProxy()

        if "proxy" in self.config:
            proxy_config=self.config["proxy"]
            if "host" in proxy_config:
                self.proxy.setHostName(proxy_config["host"])
            if "port" in proxy_config:
                self.proxy.setPort(proxy_config["port"])
            if "user" in proxy_config:
                self.proxy.setUser(proxy_config["user"])
            if "password" in proxy_config:
                self.proxy.setPassword(proxy_config["password"])
            self.proxy.setType(QNetworkProxy.HttpProxy)

        self.networkManager = QNetworkAccessManager()
        self.networkManager.setProxy(self.proxy)

        pass


class MainWidget(QtWidgets.QDialog):
    def __init__(self, app):
        super().__init__()
        self.app=app
        self.setWindowTitle("SHUI Wifi Plugin")
        self.setFixedWidth(500)
        self.setFixedHeight(300)
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setContentsMargins(2, 2, 2, 2)
        self.mainLayout.setSpacing(0)
        self.printerSelectLayout = QtWidgets.QHBoxLayout()
        self.cbPrinterSelect = QtWidgets.QComboBox(self)
        pn=[]
        for p in self.app.config["printers"]:
            pn.append(p["name"])
        self.cbPrinterSelect.addItems(pn)
        self.cbPrinterSelect.currentIndexChanged.connect(self.printerChanged)


        self.btConnect = QtWidgets.QPushButton(self)
        self.btConnect.setMaximumSize(QtCore.QSize(100, 16777215))

        self.printerSelectLayout.addWidget(self.cbPrinterSelect)
        self.printerSelectLayout.addWidget(self.btConnect)
        self.printerSelectLayout.setContentsMargins(2, 2, 2, 2)

        self.tabWidget = QtWidgets.QTabWidget(self)

        self.mainLayout.addLayout(self.printerSelectLayout)
        self.mainLayout.addWidget(self.tabWidget)

        self.makeTabs()

        self.btConnect.clicked.connect(self.doConnect)
        self.app.onUartConnect.connect(self.doOnConnect)
        self.doOnConnect(False)
        pass

    def makeTabs(self):
        self.tabs = []

        tab = FileTab(self.app)
        self.tabs.append(tab)
        self.tabWidget.addTab(tab, tab.title)

        tab = ConsoleTab(self.app)
        self.tabs.append(tab)
        self.tabWidget.addTab(tab, tab.title)

        pass

    def doConnect(self):
        if self.app.wifiUart.connected:
            self.app.wifiUart.disconnect()
        else:
            self.app.wifiUart.connect(self.app.config["printers"][self.app.selectedPrinter]["ip"])
        pass

    def doOnConnect(self, connected):
        if connected:
            self.btConnect.setText("Disconnect")
        else:
            self.btConnect.setText("Connect")

    def printerChanged(self, index):
        self.app.selectedPrinter = index
        pass

def makeForm(startMode):
    app=App(startMode)
    form = MainWidget(app)
    form.show()
    return form

def cura_application():
    return makeForm(Core.StartMode.CURA)

def qt_application(startMode):
    import sys
    application = QtWidgets.QApplication(sys.argv)
    form = makeForm(startMode)
    sys.exit(application.exec_())
