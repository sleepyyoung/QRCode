# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Prompt(object):
    def setupUi(self, Prompt):
        Prompt.setObjectName("Prompt")
        Prompt.resize(380, 254)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/yes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Prompt.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Prompt)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Prompt)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.open = QtWidgets.QPushButton(Prompt)
        self.open.setObjectName("open")
        self.gridLayout.addWidget(self.open, 1, 0, 1, 1)
        self.open_floder = QtWidgets.QPushButton(Prompt)
        self.open_floder.setObjectName("open_floder")
        self.gridLayout.addWidget(self.open_floder, 1, 1, 1, 1)
        self.ok = QtWidgets.QPushButton(Prompt)
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 1, 2, 1, 1)

        self.retranslateUi(Prompt)
        QtCore.QMetaObject.connectSlotsByName(Prompt)

    def retranslateUi(self, Prompt):
        _translate = QtCore.QCoreApplication.translate
        Prompt.setWindowTitle(_translate("Prompt", "提示"))
        self.label.setText(_translate("Prompt", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">生成成功！</span></p></body></html>"))
        self.open.setText(_translate("Prompt", "打开..."))
        self.open_floder.setText(_translate("Prompt", "打开文件夹"))
        self.ok.setText(_translate("Prompt", "OK"))
import picture_rc
