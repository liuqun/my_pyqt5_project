# -*- encoding: utf-8 -*-
import logging

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QDialog

from .my_central_widget import MyCentralWidget
# from .settings_dialog import SettingsDialog
from .Ui_MainWindow import Ui_MainWindow

# from PyQt5.QtCore import QUrl
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget

class MainWindow(QMainWindow, Ui_MainWindow):
    COMPANY_NAME = '青岛中瑞电科'
    APP_NAME = 'Video player app'

    def __init__(self):
        super().__init__()
        super(Ui_MainWindow).__init__()
        # self.toolBar = None
        self.actionOpen = None
        self.centralWidget = None
        self.setupUi(self)
        self.centralWidget = MyCentralWidget()
        ##w = QVideoWidget()
        ##w.resize(300, 300)
        ##w.move(0, 0)
        ##self.centralWidget = w
        self.setCentralWidget(self.centralWidget)
        ##self.player = QMediaPlayer()
        ##self.player.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Administrator/Videos/30-02独立按键中断例程.avi")))
        ##self.player.setVideoOutput(w)
        self.setupQtSignalConnections()

    def setupQtSignalConnections(self):
        # self.actionEditSettings.triggered.connect(self.show_settings_dialog)
        self.actionOpen.triggered.connect(self.on_action_1_triggered)

    ##def on_action_2_triggered(self):
    ##    self.player.play()
        
    def getCurrentSettings(self):
        # qs = QSettings(self.COMPANY_NAME, application=self.APP_NAME)
        # sever_address = qs.value('sever_address', 'localhost', type=str)
        # port = qs.value('port', 9999, type=int)
        # del(qs)
        # return sever_address, port
        return '127.0.0.1', 9999

    def saveSettings(self, sever_address: str, port: int):
        pass
        # qs = QSettings(self.COMPANY_NAME, application=self.APP_NAME)
        # qs.setValue('sever_address', sever_address)
        # qs.setValue('port', port)
        # del(qs)

    def on_action_1_triggered(self):
        # supportedFiletypes = self.centralWidget.mediaPlayer.supportedMimeTypes()
        # logging.error('supported filetypes={}'.format(supportedFiletypes))
        url, filetype = QFileDialog.getOpenFileUrl(self,
                                                   "选取视频文件",
                                                   ".",
                                                   "AVI Files (*.avi);;All Files (*)")
        if url is None or len(url.toString()) <= 0:
            logging.error('No video to play')
            return
        logging.error('file={}, type={}'.format(url.toLocalFile(), filetype))
        self.centralWidget.select_video_by_url(url)

    def on_connection_lost(self):
        pass

    def show_settings_dialog(self):
        pass
        # sever_address, port = self.getCurrentSettings()
        # all_settings, ok = SettingsDialog.getAllSettings(sever_address, port, self)
        # if ok:
        #     sever_address = all_settings['sever_address']
        #     port = all_settings['port']
        #     self.saveSettings(sever_address, port)
