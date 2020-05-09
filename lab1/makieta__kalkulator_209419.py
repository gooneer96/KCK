import sys
from PyQt5 import QtWidgets

class Menu(QtWidgets.QMainWindow):  
    def __init__(self):
        super(Menu, self).__init__() 
        self.setCentralWidget(Buttons(self))
        self.setWindowTitle('Kalkulator dla opornych')
        self.statusBar().showMessage('Podaj cyfre/liczbe')


class Buttons(QtWidgets.QWidget):
    def __init__(self, parent):
        super(Buttons, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QtWidgets.QGridLayout()
        grid.addWidget(QtWidgets.QLineEdit(), 0, 0, 1,3)
        names=[['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9'],
               ['+', '0',  '=']]
        for i in range (1,5):
            for j in range (0,3):
                button = QtWidgets.QPushButton(names[i-1][j])
                button.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                grid.addWidget(button, i, j)
        self.setLayout(grid)

def main():
    app = QtWidgets.QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 
