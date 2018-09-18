from player import MainWindow
from player_app_rc import qInitResources, qCleanupResources
from PyQt5.QtWidgets import QApplication
import sys


class PlayerApp(QApplication):
    def exec_(self):
        qInitResources()
        mainWindow = MainWindow()
        mainWindow.show()
        rc = super().exec_()
        qCleanupResources()
        return rc


if '__main__' == __name__:
    app = PlayerApp(sys.argv)
    rc = app.exec_()
    sys.exit(rc)
