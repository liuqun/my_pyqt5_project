from PyQt5.QtGui import QTextCursor
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QMessageBox, QWidget
from .Ui_MyWidget import Ui_MyWidget


class MyWidget(QWidget, Ui_MyWidget):
    server_chinese_encoding = 'gbk'

    def __init__(self):
        super().__init__()
        super(Ui_MyWidget).__init__()

        self.remote_ip_addr = '127.0.0.1'
        self.remote_port = 9999
        self.sock = QTcpSocket(self)

        self.isConnectedToServer = False
        self.textEdit = None
        self.lineEdit = None
        self.pushButton = None
        self.vBox = None
        self.setupUi(self)
        self.setupQtSignalConnections()

    def setupQtSignalConnections(self):
        self.pushButton.released.connect(self.push_button_event)
        self.sock.connected.connect(self.on_socket_connected)
        self.sock.disconnected.connect(self.on_socket_disconnected)
        self.sock.readyRead.connect(self.on_socket_receive)
        self.sock.bytesWritten.connect(self.on_socket_transmit)

    def add_message(self, message):
        self.textEdit.moveCursor(QTextCursor.End)
        self.textEdit.insertPlainText(message)

    def connect(self):
        if self.isConnectedToServer:
            return

        self.sock.connectToHost(self.remote_ip_addr, self.remote_port)

        if not self.sock.waitForConnected(2500):
            msg = self.sock.errorString()
            raise ConnectionError(msg)

    def push_button_event(self):
        if not self.isConnectedToServer:
            # Error
            return

        txString = self.lineEdit.text()
        if len(txString) <= 0:
            msgBoxTitle = 'Warning'
            warning = 'You must enter a message!'
            QMessageBox.critical(self, msgBoxTitle, warning)
            self.add_message('{}\n'.format(warning))
            return
        self.sock.write(txString.encode(self.server_chinese_encoding))
        self.add_message('Wrote "{}"'.format(txString))

    def on_socket_connected(self):
        self.isConnectedToServer = True
        self.lineEdit.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.add_message('Connected to {} on port {}\n'.format(self.remote_ip_addr, self.remote_port))

    def on_socket_disconnected(self):
        self.isConnectedToServer = False
        self.lineEdit.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.add_message('Disconnected from server\n')

    def on_socket_receive(self):
        rxData = self.sock.readAll()
        unicodeMsg = rxData.data().decode(self.server_chinese_encoding)
        self.add_message('Received "{}"\n'.format(unicodeMsg))

    def on_socket_transmit(self, numBytes):
        self.add_message(" ({} bytes)\n".format(numBytes))

    # noinspection PyBroadException
    def disconnect(self):
        if not self.isConnectedToServer:
            return

        self.isConnectedToServer = False
        self.sock.close()
        self.lineEdit.setEnabled(False)
        self.pushButton.setEnabled(False)
