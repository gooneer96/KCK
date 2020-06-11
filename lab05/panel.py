
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import Qt



class Panel(QWidget):
    def __init__(self,r = 10):
        super().__init__()
        self.R=r

    def setR(self,newR):
        if newR>0:
            self.R = newR


    def paintEvent(self, e):
        qp = QPainter(self)
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def drawCircles (self, qp):
        w = self.geometry().width()
        h = self.geometry().height()
        qp.setPen(QPen(Qt.red, 8, Qt.SolidLine))
        qp.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        qp.drawEllipse((w-self.R)/2,(h-self.R)/2,self.R,self.R)
