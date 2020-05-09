
import sys

from PyQt5 import QtGui,QtCore,QtWidgets
from ColorChangeDialog import ColorChangeDialog

class MainDialog(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MainDialog, self).__init__()
        self.icon = "happy.png"
        self.r = 0
        self.g = 255
        self.b = 0
        self.title = 'Dialogi'
        self.img = QtGui.QPixmap(QtGui.QImage(250, 450, QtGui.QImage.Format_ARGB32))
        
        
        self.initUI()
        
    def initUI(self):
      
        self.label = QtWidgets.QLabel()
        self.label.setScaledContents(True)
        self.updateColor()
        self.setCentralWidget(self.label)
        self.updateIcon()
        #MENU
        
        backgroundColor = QtWidgets.QAction("&Kolor okna głównego", self);
        backgroundColor.triggered.connect(self.colorChangeEvent)

        

        view = self.menuBar().addMenu("Dialog")
       
        view.addAction(backgroundColor)
        
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle(self.title)    
        self.show()
        
   
    def updateIcon(self):
    	self.setWindowIcon(QtGui.QIcon(self.icon))
    def updateColor(self):
        self.img.fill(QtGui.QColor(self.r, self.g, self.b))
        p = QtGui.QPainter(self.img)
        p.drawPixmap(self.rect(), self.img)
        p.setPen(QtGui.QPen(QtCore.Qt.gray,5))
        p.drawEllipse(90,180,80,100)
        self.label.setPixmap(self.img)
    def colorChangeEvent(self, e):
        result = ColorChangeDialog.getColor(self.r, self.g, self.b, self)
        if result[3] == True:
        	self.r = result[0]
        	self.g = result[1]
        	self.b = result[2]
        	self.updateColor()
        
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    ex = MainDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
