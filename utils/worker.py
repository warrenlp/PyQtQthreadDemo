
from PyQt5 import QtCore

import time
import threading


class Worker(QtCore.QObject):

    finished = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.poison_pill = False
        self.lock = threading.Lock()

    @QtCore.pyqtSlot()
    def process(self):
        print(f"INFO: Worker: start process: {threading.get_ident()}")
        for i in range(5):
            with self.lock:
                if self.poison_pill:
                    # print(f"INFO: cancelling thread: {threading.get_ident()}")
                    break
            print("INFO: sleep")
            time.sleep(5)

        self.finished.emit()

    @QtCore.pyqtSlot(int)
    def cancel_thread(self, result):
        print(f"INFO: cancelling thread: {result=}: {threading.get_ident()}")
        with self.lock:
            self.poison_pill = True