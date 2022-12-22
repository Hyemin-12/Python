from PyQt5 import QtWidgets

class MyWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬 GUI")
        self.resize(400, 300)
        self.show()

app = QtWidgets.QApplication([])
window = MyWindows()
app.exec_()