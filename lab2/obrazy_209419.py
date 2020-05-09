import sys
import os
from PyQt5 import QtWidgets,QtCore,QtGui

class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.panel = QtWidgets.QLabel()
        obraz = QtGui.QPixmap("python.jpg")
        self.panel.setPixmap(obraz)
        self.panel.setScaledContents(True)
        self.setCentralWidget(self.panel)
        exitAction = QtWidgets.QAction(QtGui.QIcon('2.png'), 'Zamknij', self)
        exitAction.setStatusTip('Zamknij')
        exitAction.triggered.connect(self.close)                                
        
        akcja = QtWidgets.QAction(QtGui.QIcon('1.png'), 'Otworz', self)
        akcja.setStatusTip('Otworz katalog')
        akcja.triggered.connect(self.showDialog)

        poprzedni = QtWidgets.QAction(QtGui.QIcon('3.png'), 'Poprzedni', self)
        poprzedni.setStatusTip('Poprzedni')
        poprzedni.triggered.connect(self.prevImage)
        
        nastepny = QtWidgets.QAction(QtGui.QIcon('4.png'), 'Nastepny', self)
        nastepny.setStatusTip('Nastepny')
        nastepny.triggered.connect(self.nextImage)
        
        self.statusBar()
        menubar = self.menuBar()
    
        
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        toolbar.addAction(poprzedni)
        toolbar.addAction(akcja)
        toolbar.addAction(nastepny)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()

    def showDialog(self):
        fn=QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:', "Images (*.png *.jpg)")
        imagePath=fn[0]
        path = []
        path=imagePath.split('/')
        x=len(path)-1
        self.sciezka = ''
        for i in range(x):
            self.sciezka = self.sciezka + path[i] + "/"
        i=0
        self.pliki = []
        for file in os.listdir(self.sciezka):
            if file.endswith('.png') or file.endswith('.jpg'):
                self.pliki.append(file)
                if path[len(path)-1] == file:
                    self.index = i
            i = i + 1
      
        self.obraz = QtGui.QPixmap(imagePath)
        self.panel.setScaledContents(True)
        self.panel.setPixmap(self.obraz)

    def nextImage(self):
        if len(self.pliki)-1 == self.index:
            self.index = 0
        else:
            self.index = self.index + 1
            
        self.obraz = QtGui.QPixmap(self.sciezka + self.pliki[self.index])
        self.panel.setScaledContents(True)
        self.panel.setPixmap(self.obraz)

    def prevImage(self):
        if self.index == 0:
            self.index = len(self.pliki)-1 
        else:
            self.index = self.index - 1
            
        self.obraz = QtGui.QPixmap(self.sciezka + self.pliki[self.index])
        self.panel.setScaledContents(True)
        self.panel.setPixmap(self.obraz)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
