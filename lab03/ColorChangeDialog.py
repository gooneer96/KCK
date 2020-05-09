

from PyQt5 import QtGui,QtCore,QtWidgets
class ColorChangeDialog(QtWidgets.QDialog):
    
    def __init__(self, r, g, b, parent = None):
        super(ColorChangeDialog, self).__init__(parent)
        self.setWindowTitle("Ustaw kolor okna głównego")
        self.setGeometry(100, 100, 100, 100)
        self.r = r
        self.g = g
        self.b = b
        self.initUI()

    def initUI(self):
        grid = QtWidgets.QGridLayout()
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItem("Czerwony")
        self.combobox.addItem("Zielony")
        self.combobox.addItem("Błękitny")
        self.combobox.addItem("Żółty")
        self.combobox.model().item(0).setBackground(QtGui.QColor("red"))
        self.combobox.model().item(1).setBackground(QtGui.QColor("green"))
        self.combobox.model().item(2).setBackground(QtGui.QColor("cyan"))
        self.combobox.model().item(3).setBackground(QtGui.QColor("yellow"))
        self.combobox.setFixedWidth(250)
        self.combobox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        grid.addWidget(self.combobox, 0, 0)
        
        self.setLayout(grid)
        
       
    
    @staticmethod
    def getColor(r, g, b, parent = None):
        dialog = ColorChangeDialog(r, g, b, parent)
        result = dialog.exec_()
        return (dialog.r, dialog.g, dialog.b, result == QtWidget.QDialog.Accepted)
