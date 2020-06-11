from PyQt5.QtWidgets import *
import sys
import panel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,600)
        self.title = "Kółeczko - Serwer"
        self.setWindowTitle(self.title)
        self.menubar=self.menuBar()
        view=self.menubar.addMenu("Serwer")
        serwer = QAction("Uruchom serwer", self)
        serwer.setCheckable(True)
        view.addAction(serwer)
        view.triggered[QAction].connect(self.processSerwerAction)
        w =QWidget(self)
        l =QVBoxLayout()
        self.label=QLabel()
        self.label.setText("Serwer jest wyłączony")
        self.label.setFixedSize(600,20)
        l.addWidget(self.label)
        l.addWidget(panel.Panel())
        w.setLayout(l)
        self.setCentralWidget(w)
        self.show()

    def processSerwerAction(self,q):
        if q.text()=="Uruchom serwer":
            q.setText("Zatrzymaj serwer")
            self.label.setText("Serwer jest włączony")
        else:
            q.setText("Uruchom serwer")
            self.label.setText("Serwer jest wyłączony")


    def changedValue(self):
        size = self.slider.value()
        self.panel.r=size

App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())
