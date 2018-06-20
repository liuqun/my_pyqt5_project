from PyQt5.QtWidgets import QMainWindow, QMessageBox
from .my_widget import MyWidget
from .Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super(Ui_MainWindow).__init__()
        self.toolBar = None
        self.actionConnect = None
        self.centralWidget = None
        self.setupUi(self)
        self.actionConnect.triggered.connect(self.on_action_connect_triggered)
        self.myWidget = MyWidget()
        self.myWidget.sock.disconnected.connect(self.on_connection_lost)
        self.setCentralWidget(self.myWidget)

    def on_action_connect_triggered(self):
        if self.myWidget.isConnectedToServer:
            self.myWidget.disconnect()
            return
        try:
            self.myWidget.connect()
        except ConnectionError as e:
            self.actionConnect.setChecked(False)
            msg = str(e)
            QMessageBox.critical(self, 'Error', msg)
            self.myWidget.add_message(msg + '\n')
            return

    def on_connection_lost(self):
        self.actionConnect.setChecked(False)
