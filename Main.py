from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Ui_MyWidget import Ui_MainWindow

# url = 'https//economia.awesomeapi.com.br/json/all'
# data= requests.get(url).json()
  

class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
       super(MyWidget, self).__init__(parent)
       self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()

    sys.exit(app.exec_())