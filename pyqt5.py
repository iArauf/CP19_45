import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 20
        self.top = 10
        self.width = 500
        self.height = 400
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Click Here', self)
        button.setToolTip('This s an example button')
        button.move(200,200) 
        button.clicked.connect(self.on_click)

        self.show()
        
    @pyqtSlot()
    def on_click(self):
        print('Welcome user')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  
