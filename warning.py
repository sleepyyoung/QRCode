# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(538, 448)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(538, 448))
        Form.setMaximumSize(QtCore.QSize(538, 448))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/no.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 350, 521, 81))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, -20, 521, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 28, 501, 311))
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WARN"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ff0000;\">生成失败！</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ff0000;\">生成失败！</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">系统检测到你当前输入了非英文字符，且翻译</span></p><p><span style=\" font-size:12pt;\">功能无法使用。</span></p><p><span style=\" font-size:12pt;\">解决方案：</span></p><p><span style=\" font-size:12pt;\">1.检查网络设置，确保网络连接</span></p><p><span style=\" font-size:12pt;\">2.选择样式1或样式2生成二维码</span></p><p><span style=\" font-size:12pt;\">3.输入英文</span></p></body></html>"))
import picture_rc
