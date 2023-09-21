
from .main import Ui_MainWindow
from .main_dialog import MainDialog

from PyQt5 import QtCore, QtWidgets


class MainWindow(Ui_MainWindow, QtCore.QObject):

    def __init__(self, main_window):
        Ui_MainWindow.__init__(self)
        QtCore.QObject.__init__(self)
        self.setupUi(main_window)
        self.main_window = main_window

        self.launchButton.clicked.connect(self.launch_dialog)

        self.dialog_end = False

    @QtCore.pyqtSlot()
    def launch_dialog(self):
        qdialog = QtWidgets.QDialog(self.main_window)
        MainDialog(qdialog)
        result = qdialog.exec()

        print(f"Result: {result}")

