from client import MainWindow
from client_app_rc import qInitResources, qCleanupResources
from PyQt5.QtWidgets import QApplication
import sys


class ClientApp(QApplication):
    def exec_(self):
        qInitResources()
        mainWindow = MainWindow()
        mainWindow.show()
        rc = super().exec_()
        qCleanupResources()
        return rc


if '__main__' == __name__:
    app = ClientApp(sys.argv)
    rc = app.exec_()
    sys.exit(rc)
