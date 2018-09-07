from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from .Ui_MyCentralWidget import Ui_MyCentralWidget
import logging


class MyCentralWidget(QWidget, Ui_MyCentralWidget):
    def __init__(self):
        super().__init__()
        super(Ui_MyCentralWidget).__init__()
        self.videoWidget = None
        self.setupUi(self)

        self.videoWidget.setStyleSheet("image: url(:/images/settings.png);")

        from PyQt5.QtMultimedia import QMediaPlayer
        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.setupQtSignalConnections()

    def setupQtSignalConnections(self):
        self.pushButton.clicked.connect(self.push_button_callback)
        self.mediaPlayer.error.connect(self.media_player_error_handler_callback)
        self.mediaPlayer.mediaStatusChanged.connect(self.media_player_status_watcher_callback)

    def select_video_by_url(self, url:QUrl):
        self.label.setText(url.toLocalFile())
        self.mediaPlayer.setMedia(QMediaContent(url))

    # def pause_button_callback(self):
    #     statusCode = self.mediaPlayer.state()
    #     if statusCode == QMediaPlayer.PlayingState:
    #         self.mediaPlayer.pause()
    #         self.pushButton.setEnabled(False)
    #         return

    def push_button_callback(self):
        statusCode = self.mediaPlayer.state()
        logging.error('statusCode={}'.format(statusCode))
        logging.error('--QMediaPlayer.PlayingState={}'.format(QMediaPlayer.PlayingState))
        logging.error('--QMediaPlayer.PausedState={}'.format(QMediaPlayer.PausedState))
        logging.error('--QMediaPlayer.StoppedState={}'.format(QMediaPlayer.StoppedState))
        if statusCode == QMediaPlayer.PausedState or statusCode == QMediaPlayer.StoppedState:
            self.mediaPlayer.play()
            return
        logging.error('Unexpected statusCode={}'.format(statusCode))

    def media_player_error_handler_callback(self, errorCode):
        logging.error('media_player_error_handler_callback ok')
        logging.error('errorCode={}'.format(errorCode))

    def media_player_status_watcher_callback(self, statusCode):
        logging.error('media_player_status_watcher_callback ok')
        logging.error('status={}'.format(statusCode))
        logging.error('--QMediaPlayer.InvalidMedia={}'.format(QMediaPlayer.InvalidMedia))
        logging.error('--QMediaPlayer.LoadedMedia={}'.format(QMediaPlayer.LoadedMedia))
        logging.error('--QMediaPlayer.EndOfMedia={}'.format(QMediaPlayer.EndOfMedia))
        if statusCode == QMediaPlayer.LoadedMedia:
            self.mediaPlayer.play()
            return
        self.pushButton.setEnabled(False)
        if statusCode == QMediaPlayer.InvalidMedia:
            reply = QMessageBox.warning(self, '无法播放', '缺少视频解码插件', QMessageBox.Ok)
            return
        if statusCode == QMediaPlayer.EndOfMedia:
            self.pushButton.setEnabled(True)
            self.pauseButton.setEnabled(False)
            return
        if statusCode == QMediaPlayer.BufferedMedia:
            self.pauseButton.setEnabled(True)
        return

