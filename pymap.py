import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from ip import Ip

qt_creator_file = "pymap.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Pymap GUI")
        self.start_scan.pressed.connect(self.scan)

    # When pushing the scan button, get the IP from the text area
    def scan(self):
        ip = self.ip_input.text()
        r = Ip(ip)
        r.check_ip(ip)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()