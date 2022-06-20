# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test/test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(185, 198)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        self.toolButton_3.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout_2.addWidget(self.toolButton_3, 1, 0, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_2.addWidget(self.toolButton_2, 1, 2, 1, 1)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 1, 1, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout_2.addWidget(self.toolButton_4, 0, 1, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(Form)
        self.toolButton_5.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout_2.addWidget(self.toolButton_5, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton_3.setText(_translate("Form", "..."))
        self.toolButton_2.setText(_translate("Form", "..."))
        self.toolButton.setText(_translate("Form", "..."))
        self.toolButton_4.setText(_translate("Form", "..."))
        self.toolButton_5.setText(_translate("Form", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
