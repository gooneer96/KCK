
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import Qt



class Panel(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        qp = QPainter(self)
        self.r=100
        qp.begin(self)
        qp.setPen(QPen(Qt.red, 8, Qt.SolidLine))
        qp.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        qp.drawEllipse(250, 250, 200, 200)
