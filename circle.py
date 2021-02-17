import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.st = False
        self.color = ['yellow', 'blue', 'black', 'Green', 'Brown', 'Red', 'Orange', 'Pink']

    def initUI(self):
        self.setGeometry(300, 300, 600, 500)

        self.btn = QPushButton('Нарисовать', self)
        self.btn.setGeometry(20, 20, 80, 40)
        self.btn.move(270, 420)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.st:
            qp = QPainter()
            qp.begin(self)
            self.circle(qp)
            qp.end()

    def paint(self):
        self.st = True
        self.repaint()

    def circle(self, qp):
        a = random.randrange(50, 200)
        qp.setBrush(QColor(random.choice(self.color)))
        qp.drawEllipse(300, 100, a, a)
        qp.setBrush(QColor(random.choice(self.color)))
        a = random.randrange(50, 200)
        qp.setBrush(QColor(random.choice(self.color)))
        qp.drawEllipse(250, 300, a, a)
        a = random.randrange(50, 200)
        qp.setBrush(QColor(random.choice(self.color)))
        qp.drawEllipse(100, 40, a, a)
        a = random.randrange(50, 200)
        qp.setBrush(QColor(random.choice(self.color)))
        qp.drawEllipse(50, 350, a, a)
        a = random.randrange(50, 200)
        qp.setBrush(QColor(random.choice(self.color)))
        qp.drawEllipse(500, 300, a, a)
        self.st = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
