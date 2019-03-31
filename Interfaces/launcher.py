import sys

from PyQt5 import QtWidgets

try:
    from ctrl_login import MainWindow
except Exception as e:
    from Interfaces.ctrl_login import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
