from PyQt5.QtCore import Qt, QSize, QThread, pyqtProperty, QPointF
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QToolBar, QApplication, QAction, QActionGroup, QGridLayout, \
    QWidget
import threading,time
import sys

#Startowo ruch jest wyłączony, zgodnie z zadaniem 4 należy ustawić kursor "Gwiazdka" i możliwe będzie wystartowanie "mordek" za pomocą toolbaru


class Face(QLabel):
  def __init__(self, parent,icon_fn):
    super().__init__(parent)
    pix = QPixmap(icon_fn)
    self.setPixmap(pix)

  def _set_pos(self, pos):
    self.move(pos.x() - self.w/2, pos.y() - self.h/2)
  pos = pyqtProperty(QPointF, fset=_set_pos)


class Panel(QWidget):
    def __init__(self, icon_fn):
        super().__init__()
        self.face = Face(self, icon_fn)
        self.face.setScaledContents(True)
        self.face.move(10,1)
        self.face.resize(50,50)
        self.show


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.width=500
        self.height=300
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle("Main window")
        self.setWindowIcon(QIcon('happy.png'))
        self.initUI()


    def initUI(self):

        lay = QGridLayout()

        self.panelHappy = Panel("happy.png")
        self.panelNeutral = Panel("neutral.png")

        self.panelSad = Panel("sad.png")

        lay.addWidget(self.panelHappy,0,0)
        lay.addWidget(self.panelNeutral,1,0)
        lay.addWidget(self.panelSad, 2 ,0)

        w = QWidget()
        w.setLayout(lay)
        self.setCentralWidget(w)


        self.menubar = self.menuBar()

        view = self.menubar.addMenu("Widok")

        self.cursors = self.menubar.addMenu("Kursory")

        self.cursors.menuAction().setVisible(False)

        actionGroup = QActionGroup(self)
        arrowAction=QAction("Strzałka", self)
        arrowAction.setCheckable(True)
        arrowAction.setChecked(True)
        arrow= actionGroup.addAction(arrowAction)
        self.cursors.addAction(arrow)
        waitAction=QAction("Klepsydra", self)
        waitAction.setCheckable(True)
        wait= actionGroup.addAction(waitAction)
        self.cursors.addAction(wait)
        self.cursors.addSeparator()
        crossAction=QAction("Gwiazdka", self)
        crossAction.setCheckable(True)
        cross= actionGroup.addAction(crossAction)
        self.cursors.addAction(cross)
        self.cursors.triggered[QAction].connect(self.processTriggerCursors)
        cursorMenu = QAction("Pokaż menu z kursorami", self)
        view.addAction(cursorMenu)



        toolbarAction = QAction("Toolbar",self)
        toolbarAction.setShortcut("Alt+M")
        toolbarAction.setCheckable(True)
        toolbarAction.setChecked(True)
        view.addAction(toolbarAction)

        view.triggered[QAction].connect(self.processTriggerView)

        self.toolbar = QToolBar("My main toolbar")
        self.addToolBar(self.toolbar)

        self.button_happy = QAction(QIcon('happy.png'),"Happy", self)
        self.button_happy.triggered.connect(self.happyFaceMove)
        self.button_happy.setCheckable(True)
        self.button_happy.setChecked(False)
        self.button_happy.setEnabled(False)
        self.toolbar.addAction(self.button_happy)

        self.button_neutral = QAction(QIcon('neutral.png'),"Neutral", self)
        self.button_neutral.triggered.connect(self.neutralFaceMove)
        self.button_neutral.setCheckable(True)
        self.button_neutral.setChecked(False)
        self.button_neutral.setEnabled(False)
        self.toolbar.addAction(self.button_neutral)

        self.button_sad = QAction(QIcon('sad.png'),"Sad", self)
        self.button_sad.triggered.connect(self.sadFaceMove)
        self.button_sad.setCheckable(True)
        self.button_sad.setChecked(False)
        self.button_sad.setEnabled(False)
        self.toolbar.addAction(self.button_sad)

        self.show()

        x=threading.Thread(target=self.threadHappy,daemon=True)  #daemon=True aby zakończyć pracę wątku gdy zakończone zostaną wszystkię wątki nie-daemon, czyli po zamknięciu GUI, ubite zostaną też wątki od ruchu mordek
        x.start()
        x1=threading.Thread(target=self.threadNeutral,daemon=True)
        x1.start()
        x2=threading.Thread(target=self.threadSad,daemon=True)
        x2.start()

    def threadHappy(self):
        x = 50
        direction = 1
        while True:
            while self.button_happy.isChecked() is False:
                time.sleep(0.1)
            if x>420:
                direction = -1
            elif x<1:
                direction = 1
            x += direction
            self.panelHappy.face.move(x,1)
            time.sleep(0.01)


    def threadNeutral(self):
        x = 50
        direction = 1
        while True:
            while self.button_neutral.isChecked() is False:
                time.sleep(0.1)
            if x>420:
                direction = -1
            elif x<1:
                direction = 1
            x += direction
            self.panelNeutral.face.move(x,1)
            time.sleep(0.03)

    def threadSad(self):
        x = 50
        direction = 1
        while True:
            while self.button_sad.isChecked() is False:
                time.sleep(0.1)
            if x>420:
                direction = -1
            elif x<1:
                direction = 1
            x += direction
            self.panelSad.face.move(x,1)
            time.sleep(0.05)

    def happyFaceMove(self, s):
        if self.cursor()==QCursor(Qt.WaitCursor):
            if s is False:
                self.button_happy.setEnabled(False)
            else:
                self.button_happy.setEnabled(True)
        elif self.cursor()==self.current_cursor:
            if s is True:
                self.button_happy.setEnabled(False)
            else:
                self.button_happy.setEnabled(True)

    def neutralFaceMove(self, s):
        if self.cursor()==QCursor(Qt.WaitCursor):
            if s is False:
                self.button_neutral.setEnabled(False)
            else:
                self.button_neutral.setEnabled(True)
        elif self.cursor()==self.current_cursor:
            if s is True:
                self.button_neutral.setEnabled(False)
            else:
                self.button_neutral.setEnabled(True)

    def sadFaceMove(self, s):
        if self.cursor()==QCursor(Qt.WaitCursor):
            if s is False:
                self.button_sad.setEnabled(False)
            else:
                self.button_sad.setEnabled(True)
        elif self.cursor()==self.current_cursor:
            if s is True:
                self.button_sad.setEnabled(False)
            else:
                self.button_sad.setEnabled(True)

    def processTriggerView(self, q):
        if q.text()=="Toolbar":
            self.toolbar.setVisible(True)
            if q.isChecked() is False:
                self.toolbar.setVisible(False)
        elif q.text()=="Pokaż menu z kursorami":
            q.setText("Ukryj menu z kursorami")
            self.cursors.menuAction().setVisible(True)
        elif q.text()=="Ukryj menu z kursorami":
            q.setText("Pokaż menu z kursorami")
            self.cursors.menuAction().setVisible(False)
        else:
            print(1)

    def processTriggerCursors(self, q):
        if q.text()=="Strzałka":
                self.setCursor(QCursor(Qt.ArrowCursor))
                self.button_happy.setEnabled(False)
                self.button_neutral.setEnabled(False)
                self.button_sad.setEnabled(False)
        elif q.text()=="Klepsydra":
            if q:
                self.setCursor(QCursor(Qt.WaitCursor))
                if self.button_happy.isChecked():
                    self.button_happy.setEnabled(True)
                else:
                    self.button_happy.setEnabled(False)
                if self.button_neutral.isChecked():
                    self.button_neutral.setEnabled(True)
                else:
                    self.button_neutral.setEnabled(False)
                if self.button_sad.isChecked():
                    self.button_sad.setEnabled(True)
                else:
                    self.button_sad.setEnabled(False)
        else:
            if q:
                self.cursor_pix= QPixmap('cursor.png')
                self.cursor_scaled_pix = self.cursor_pix.scaled(QSize(30, 30), Qt.KeepAspectRatio)
                self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)
                self.setCursor(self.current_cursor)
                if self.button_happy.isChecked() is False:
                    self.button_happy.setEnabled(True)
                else:
                    self.button_happy.setEnabled(False)
                if self.button_neutral.isChecked() is False:
                    self.button_neutral.setEnabled(True)
                else:
                    self.button_neutral.setEnabled(False)
                if self.button_sad.isChecked() is False:
                    self.button_sad.setEnabled(True)
                else:
                    self.button_sad.setEnabled(False)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
