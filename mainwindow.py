from warning import Ui_Form
from success import Ui_Prompt
from ui import Ui_QRCode
import pyglet
import cv2
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import style1
import style2
import style3
import translate
import globalvar
import os
import time
import picture_rc

globalvar._init()
gif_path='_'
class MainWindow(QMainWindow):
    global gif_path
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_QRCode()
        self.ui.setupUi(self)

        self.ui.generate.setEnabled(False)
        self.ui.select_picture.clicked.connect(self.loadFile)
        self.ui.select_path.clicked.connect(self.loadText)
        self.ui.comboBox.currentIndexChanged.connect(self.comboBox_Changed)
        self.ui.icon_path.textChanged.connect(self.icon_path_Changed)
        self.ui.generate.clicked.connect(self.create)

    def loadFile(self):
        fname, _ = QFileDialog.getOpenFileName(None, 'select pictures', '/', 'Image files(*.jpg *.gif *.png *.bmp *.tga)')
        # 此处将'self'改为'None'，但不知为何...
        self.ui.picture.setPixmap(QPixmap(fname))
        self.ui.icon_path.setText(fname)

    def loadText(self):
        fname= QFileDialog.getExistingDirectory(None,'select floder','/')
        self.ui.save_path.setText(fname)

    def jump_to_warning(self):
        warnwindow.open()

    def jump_to_success(self):
        successwindow.open()

    def icon_path_Changed(self):
        self.ui.generate.setEnabled(True)

    def comboBox_Changed(self):
        x = self.ui.comboBox.currentText()
        if x == '样式1':
            self.ui.generate.setEnabled(True)
        else:
            picture_path = self.ui.icon_path.toPlainText()
            if picture_path == 'NULL':
                self.ui.generate.setEnabled(False)
            else:
                self.ui.generate.setEnabled(True)
        QApplication.processEvents()
        time.sleep(0.01)

    def GetDesktopPath(self):
      return os.path.join(os.path.expanduser("~"), 'Desktop')

    def create(self):
        data=self.ui.contents.toPlainText()
        save_path = self.ui.save_path.toPlainText()
        if save_path=="（默认为桌面）":
            save_path=self.GetDesktopPath()

        x = self.ui.comboBox.currentText()
        if x == '样式1':
            self.ui.generate.setEnabled(True)
            style1.make_qrcode(data,  save_path)
            self.jump_to_success()
        if x == '样式2':
            picture_path = self.ui.icon_path.toPlainText()
            style2.make_qrcode(data, picture_path, save_path)
            self.jump_to_success()
        if x == '样式3':
            picture_path = self.ui.icon_path.toPlainText()
            if style3.is_Chinese(data):
                try:
                    data=translate.tran(data)
                except:
                    self.jump_to_warning()
            try:
                style3.make_qrcode(data, picture_path, save_path)
                self.jump_to_success()
            except:
                pass

    def picture_floder(self):
        save_path = self.ui.save_path.toPlainText()
        if save_path == "（默认为桌面）":
            save_path = self.GetDesktopPath()
        QFileDialog.getOpenFileName(None,'THIS',str(save_path))

    def show_picture(self):
        save_path = self.ui.save_path.toPlainText()
        if save_path == "（默认为桌面）":
            save_path = self.GetDesktopPath()
        else:
            save_path = self.ui.save_path.toPlainText()
            
        picture_path=save_path+"\\"+globalvar.get_value('key')
        gif_path=picture_path.replace('\\','/')

        if gif_path.split('.')[-1]=='gif':
            qrpath,qrname = os.path.split(gif_path)
            # print(qrpath,qrname)
            pyglet.resource.path=[qrpath]
            pyglet.resource.reindex()
            animation = pyglet.resource.animation(qrname)
            sprite = pyglet.sprite.Sprite(animation)
            win = pyglet.window.Window(width=sprite.width, height=sprite.height)
            @win.event
            def on_draw():
                win.clear()
                sprite.draw()
            pyglet.app.run()
        else:
            image=cv2.imread(picture_path)
            cv2.namedWindow("PICTURE",cv2.WINDOW_AUTOSIZE)
            cv2.moveWindow("PICTURE",800,300)
            cv2.imshow('PICTURE',image)

class WarnWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)

    def open(self):
        self.show()

class SuccessWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_Prompt()
        self.ui.setupUi(self)

        self.ui.open.clicked.connect(self.open_picture)
        self.ui.open_floder.clicked.connect(self.open_floder)
        self.ui.ok.clicked.connect(self.close)

    def open_picture(self):
        mainwindow.show_picture()
    def open_floder(self):
        mainwindow.picture_floder()

    def open(self):
        self.show()

if __name__ == '__main__':
     app = QApplication(sys.argv)
     mainwindow=MainWindow()
     mainwindow.setFixedSize(565,544);
     warnwindow=WarnWindow()
     warnwindow.setFixedSize(538, 448)
     warnwindow.setWindowFlags(Qt.WindowStaysOnTopHint)
     warnwindow.setWindowModality(Qt.ApplicationModal)
     successwindow=SuccessWindow()
     successwindow.setFixedSize(380,254)

     mainwindow.show()
     sys.exit(app.exec_())
