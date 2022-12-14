from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
# import sloty

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        x=0
        self.label.setText("you clicked me!" + str(x)) # ustawianie tekstu labelki
        x+=1
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Test Window")

        #labelki
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label1")
        self.label.move(50,35) #położenie labelki od lewego górnego rogu (x,y)


        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText("label4")
        self.label4.move(50,50)

        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText("label7")
        self.label7.move(50,65)
        

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked) # łączenie przycisku z funkcją

    def update(self):
        self.label.adjustSize() # dopasowywanie wielkości do zawartości


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
