
from PyQt5 import QtCore

from .threading_dialog import Ui_Dialog
from utils.worker import Worker

import threading

class MainDialog(Ui_Dialog, QtCore.QObject):

    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        QtCore.QObject.__init__(self)
        self.setupUi(dialog)

        original_show_event = dialog.showEvent

        def showEvent(event: QtCore.QEvent):
            original_show_event(event)
            self.start_background_thread()

        dialog.showEvent = showEvent

        self.thread = None
        self.worker = None

        self.dialog = dialog

    def start_background_thread(self):
        print(f"INFO: start_background_thread: {threading.get_ident()}")
        self.thread = QtCore.QThread()
        self.worker = Worker()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.process)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # It is very important to force a DirectConnection as the target thread is locked up by a long-running process.
        self.dialog.finished.connect(self.worker.cancel_thread, QtCore.Qt.DirectConnection)

        self.thread.start()
