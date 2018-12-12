import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from guess_number import Ui_MainWindow


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
