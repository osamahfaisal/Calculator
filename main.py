
#  import labriry 
from PyQt5 import QtCore, QtGui, QtWidgets
from Calculator import Ui_Form   # name of folder contain class then import class 
import sys


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)


# methods of bush button 
def zero():
    # ui.screan.text() take text in the lineEdit and add zero  to it 
    ui.screan.setText(ui.screan.text() + "0")
    
def one():
    ui.screan.setText(ui.screan.text() + "1")
    
def two():
    ui.screan.setText(ui.screan.text() + "2")
    
def three():
    ui.screan.setText(ui.screan.text() + "3")


def four():
    ui.screan.setText(ui.screan.text() + "4")
    
def five():
    ui.screan.setText(ui.screan.text() + "5")
    
def six():
    ui.screan.setText(ui.screan.text() + "6")


def seven():
    ui.screan.setText(ui.screan.text() + "7")
    
def eight():
    ui.screan.setText(ui.screan.text() + "8")
    
def nine():
    ui.screan.setText(ui.screan.text() + "9")


def dot():
    ui.screan.setText(ui.screan.text() + ".")


def  maltyplay():
    ui.screan.setText(ui.screan.text() + "*")
    
def  division():
    ui.screan.setText(ui.screan.text() + "/")


def subtract():
    ui.screan.setText(ui.screan.text() + "-")

def add():
    ui.screan.setText(ui.screan.text() + "+")
    

def equal():
    x=ui.screan.text() 
    equ=str(eval(x))
    ui.screan.setText(equ)





#  program from here    
if __name__ == "__main__":
    
    #   to  connect button by methods  
    ui.numberTwoPushButton_5.clicked.connect(zero)
    ui.numberOnePushButton_2.clicked.connect(one)
    ui.numberTwoPushButton_2.clicked.connect(two)
    ui.numberThreePushButton_2.clicked.connect(three)
    ui.numberFourPushButton_2.clicked.connect(four)
    ui.numberFivePushButton_2.clicked.connect(five)
    ui.numberSixPushButton_2.clicked.connect(six)
    ui.numberSevenPushButton_2.clicked.connect(seven)
    ui.numberEightPushButton_2.clicked.connect(eight)
    ui.numberNinePushButton_2.clicked.connect(nine)
    ui.numberOnePushButton_5.clicked.connect(dot)
    ui.multiplyPushButton.clicked.connect(maltyplay)
    ui.divisionPushButton_2.clicked.connect(division)
    ui.subtractionPushButton_2.clicked.connect(subtract)
    ui.multiplyPushButton_5.clicked.connect(add)
    
    ui.numberThreePushButton_5.clicked.connect(equal)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    Form.show()
    sys.exit(app.exec_())