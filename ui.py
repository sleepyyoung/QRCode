# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QRCode(object):
    def setupUi(self, QRCode):
        QRCode.setObjectName("QRCode")
        QRCode.resize(565, 544)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/qqq.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QRCode.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(QRCode)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(553, 514))
        self.tabWidget.setMaximumSize(QtCore.QSize(553, 514))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.select_picture = QtWidgets.QPushButton(self.tab)
        self.select_picture.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.select_picture.setObjectName("select_picture")
        self.label_style = QtWidgets.QLabel(self.tab)
        self.label_style.setGeometry(QtCore.QRect(40, 110, 161, 21))
        self.label_style.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_style.setObjectName("label_style")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(220, 110, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label3 = QtWidgets.QLabel(self.tab)
        self.label3.setGeometry(QtCore.QRect(330, 240, 81, 21))
        self.label3.setTextFormat(QtCore.Qt.RichText)
        self.label3.setScaledContents(False)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setWordWrap(False)
        self.label3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label3.setObjectName("label3")
        self.style1 = QtWidgets.QLabel(self.tab)
        self.style1.setEnabled(True)
        self.style1.setGeometry(QtCore.QRect(130, 150, 81, 81))
        self.style1.setMouseTracking(True)
        self.style1.setTabletTracking(False)
        self.style1.setText("")
        self.style1.setPixmap(QtGui.QPixmap(":/style1.png"))
        self.style1.setScaledContents(True)
        self.style1.setObjectName("style1")
        self.label2 = QtWidgets.QLabel(self.tab)
        self.label2.setGeometry(QtCore.QRect(230, 240, 81, 21))
        self.label2.setTextFormat(QtCore.Qt.RichText)
        self.label2.setScaledContents(False)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setWordWrap(False)
        self.label2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label2.setObjectName("label2")
        self.label1 = QtWidgets.QLabel(self.tab)
        self.label1.setGeometry(QtCore.QRect(130, 240, 81, 21))
        self.label1.setTextFormat(QtCore.Qt.RichText)
        self.label1.setScaledContents(False)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label1.setObjectName("label1")
        self.style3 = QtWidgets.QLabel(self.tab)
        self.style3.setEnabled(True)
        self.style3.setGeometry(QtCore.QRect(330, 150, 81, 81))
        self.style3.setMouseTracking(True)
        self.style3.setTabletTracking(False)
        self.style3.setText("")
        self.style3.setPixmap(QtGui.QPixmap(":/style3.png"))
        self.style3.setScaledContents(True)
        self.style3.setObjectName("style3")
        self.style2 = QtWidgets.QLabel(self.tab)
        self.style2.setEnabled(True)
        self.style2.setGeometry(QtCore.QRect(230, 150, 81, 81))
        self.style2.setMouseTracking(True)
        self.style2.setTabletTracking(False)
        self.style2.setText("")
        self.style2.setPixmap(QtGui.QPixmap(":/style2.png"))
        self.style2.setScaledContents(True)
        self.style2.setObjectName("style2")
        self.picture = QtWidgets.QLabel(self.tab)
        self.picture.setGeometry(QtCore.QRect(330, 20, 81, 81))
        self.picture.setText("")
        self.picture.setTextFormat(QtCore.Qt.AutoText)
        self.picture.setScaledContents(True)
        self.picture.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.picture.setWordWrap(False)
        self.picture.setIndent(-1)
        self.picture.setOpenExternalLinks(False)
        self.picture.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.picture.setObjectName("picture")
        self.icon_path = QtWidgets.QTextEdit(self.tab)
        self.icon_path.setGeometry(QtCore.QRect(10, 50, 231, 31))
        self.icon_path.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.icon_path.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.icon_path.setObjectName("icon_path")
        self.select_path = QtWidgets.QPushButton(self.tab)
        self.select_path.setGeometry(QtCore.QRect(30, 420, 131, 31))
        self.select_path.setObjectName("select_path")
        self.save_path = QtWidgets.QTextEdit(self.tab)
        self.save_path.setGeometry(QtCore.QRect(170, 420, 271, 31))
        self.save_path.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.save_path.setObjectName("save_path")
        self.generate = QtWidgets.QPushButton(self.tab)
        self.generate.setGeometry(QtCore.QRect(460, 420, 61, 31))
        self.generate.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.generate.setAutoFillBackground(False)
        self.generate.setObjectName("generate")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 270, 311, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.contents = QtWidgets.QTextEdit(self.tab)
        self.contents.setGeometry(QtCore.QRect(40, 303, 481, 91))
        self.contents.setObjectName("contents")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        QRCode.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QRCode)
        self.statusbar.setObjectName("statusbar")
        QRCode.setStatusBar(self.statusbar)
        self.style2.setBuddy(self.style2)

        self.retranslateUi(QRCode)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QRCode)
        QRCode.setTabOrder(self.comboBox, self.select_picture)
        QRCode.setTabOrder(self.select_picture, self.icon_path)
        QRCode.setTabOrder(self.icon_path, self.select_path)
        QRCode.setTabOrder(self.select_path, self.save_path)
        QRCode.setTabOrder(self.save_path, self.generate)

    def retranslateUi(self, QRCode):
        _translate = QtCore.QCoreApplication.translate
        QRCode.setWindowTitle(_translate("QRCode", "二维码生成器"))
        self.select_picture.setText(_translate("QRCode", "选择图片"))
        self.label_style.setText(_translate("QRCode", "请选择生成样式："))
        self.comboBox.setItemText(0, _translate("QRCode", "请选择"))
        self.comboBox.setItemText(1, _translate("QRCode", "样式1"))
        self.comboBox.setItemText(2, _translate("QRCode", "样式2"))
        self.comboBox.setItemText(3, _translate("QRCode", "样式3"))
        self.label3.setText(_translate("QRCode", "样 式 3"))
        self.style1.setToolTip(_translate("QRCode", "<html><head/><body><p><img src=\":/style1.png\"/></p></body></html>"))
        self.label2.setText(_translate("QRCode", "     样 式 2"))
        self.label1.setText(_translate("QRCode", "     样 式 1"))
        self.style3.setToolTip(_translate("QRCode", "<html><head/><body><p><img src=\":/style3.png\"/></p></body></html>"))
        self.style2.setToolTip(_translate("QRCode", "<html><head/><body><p><img src=\":/style2.png\"/></p></body></html>"))
        self.icon_path.setHtml(_translate("QRCode", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">NULL</span></p></body></html>"))
        self.select_path.setText(_translate("QRCode", "请选择保存位置"))
        self.save_path.setHtml(_translate("QRCode", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e7e7e7;\">（默认为桌面）</span></p></body></html>"))
        self.generate.setText(_translate("QRCode", "生成"))
        self.label.setText(_translate("QRCode", "请输入内容：（句子或网站链接都可）"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("QRCode", "生成"))
        self.textBrowser.setHtml(_translate("QRCode", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">1.</span><span style=\" font-size:14pt;\">样式1、样式2的二维码内容可以为汉字或英文，样式3的二维码内容只能为英文，如果输入汉字，系统将会自动翻译成英文</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">2.</span><span style=\" font-size:14pt;\">由于系统翻译英文采用在线爬取翻译结果的方式，所以选择样式3的二维码时，要么确保电脑联网，要么就别输入除英文以外的其他语言</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">3.</span><span style=\" font-size:14pt;\">默认生成图片格式为.png,只有样式3可以生成.gif二维码</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">4.</span><span style=\" font-size:14pt;\">默认生成图片名称为当前时间(如20200202020202.png/gif)</span><span style=\" font-size:6pt;\">(</span><span style=\" font-size:6pt; color:#ffaaff;\">2020年2月2日2点02分02秒</span><span style=\" font-size:6pt;\">）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">5.</span><span style=\" font-size:14pt;\">可能某些地方还有一些小Bug时不时就会跑出来，那就关了重新打开...(重启万岁)</span><span style=\" font-size:6pt;\">[</span><span style=\" font-size:6pt; color:#00ffff;\">世界上有80%的问题是可以通过重启解决的，剩下的20%？那不用解决。世界上哪有问题能100%解决啊...</span><span style=\" font-size:6pt; color:#55ff7f;\">(小声哔哔)</span><span style=\" font-size:6pt;\">]</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("QRCode", "使用说明"))
        
import picture_rc
