import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

from UI import Ui_MainWindow

from random import randint


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()

        self.setupUi(self)

        self.isdraw = False

        self.pushButton.clicked.connect(self.btnShow_click)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_square(qp)
        qp.end()

    def btnShow_click(self):
        self.isdraw = True
        self.repaint()

    def draw_square(self, qp):
        if self.isdraw:
            for i in range(15):
                qp.setBrush(QColor(255, 255, 0))

                side = randint(2, 5)
                razm = randint(5, 60)
                s = razm * side
                x = randint(1, 800)
                while x + s > 800:
                    x = randint(1, 800)
                y = randint(1, 600)
                while y + s > 600:
                    y = randint(1, 600)
                qp.drawEllipse(x, y, s, s)

        self.isdraw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
