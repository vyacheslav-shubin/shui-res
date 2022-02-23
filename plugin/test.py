import sys
import json
from PyQt5 import (QtCore)
from PyQt5.QtNetwork import (QHttpMultiPart, QHttpPart, QNetworkRequest, QNetworkAccessManager, QNetworkReply, QNetworkProxy)
from PyQt5 import (QtCore, QtWidgets)

application = QtWidgets.QApplication(sys.argv)

class Loader(QtCore.QObject):

    def handleResponse(self):
        er = self.reply.error()
        if er == QNetworkReply.NoError:
            data = json.loads(str(self.reply.readAll(), 'utf-8'))
            print(data["href"])
            print(data["method"])
        else:
            print("Error occured: ", er)
            print(self.reply.errorString())
        QtCore.QCoreApplication.quit()

    def onUploadProgress(self, bytes_sent, bytes_total):
        pass

    def onSslError(self, reply, sslerror):
        pass



    def save(self, rows):
        self.rows = rows
        self.proxy=QNetworkProxy()
        self.proxy.setHostName("proxy.krista.ru")
        self.proxy.setPort(8080)
        self.proxy.setPassword("shubin_password")
        self.proxy.setUser("shubin")
        self.proxy.setType(QNetworkProxy.HttpProxy)
        self.networkManager = QNetworkAccessManager()
        self.networkManager.setProxy(self.proxy)

        self.request = QNetworkRequest(QtCore.QUrl("https://cloud-api.yandex.net/v1/disk/resources/upload?path=app:/a.html"))
        self.request.setRawHeader(b'Accept', b'application/json')
        self.request.setRawHeader(b'Authorization', b'OAuth AQAAAAAX2tMUAAcPXPmfLJQBBkX2vxUft8UKfLI')

        self.reply = self.networkManager.get(self.request)

        self.reply.finished.connect(self.handleResponse)
        self.reply.uploadProgress.connect(self.onUploadProgress)
        self.reply.sslErrors.connect(self.onSslError)

loader = Loader()
loader.save(None)


sys.exit(application.exec_())
