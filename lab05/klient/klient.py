from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import panel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,600)
        self.title = "Kółeczko - Klient"
        self.setWindowTitle(self.title)
        self.menubar=self.menuBar()
        view=self.menubar.addMenu("Połączenie")
        polaczenie = QAction("Połącz z serwerem", self)
        view.addAction(polaczenie)
        w =QWidget(self)
        l =QVBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(10)
        self.slider.setMaximum(100)
        l.addWidget(self.slider)
        l.addWidget(panel.Panel())
        self.slider.valueChanged.connect(self.changedValue)
        w.setLayout(l)
        self.setCentralWidget(w)
        self.show()

    def changedValue(self):
        size = self.slider.value()
        self.panel.r=size
        print(size)

App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())
