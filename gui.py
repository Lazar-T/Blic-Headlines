import sys
import webbrowser
from PySide.QtCore import *
from PySide.QtGui import *
import scrapingBlic


def openFirstStory():
    webbrowser.open(href1)


def openSecondStory():
    webbrowser.open(href2)


def openThirdStory():
    webbrowser.open(href3)


def openForthStory():
    webbrowser.open(href4)


def openFifthStory():
    webbrowser.open(href5)


text1, href1 = scrapingBlic.firstHeadline()
text2, href2 = scrapingBlic.secondHeadline()
text3, href3 = scrapingBlic.thirdHeadline()
text4, href4 = scrapingBlic.forthHeadline()
text5, href5 = scrapingBlic.fifthHeadline()


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.button1 = QPushButton(text1)
        self.button2 = QPushButton(text2)
        self.button3 = QPushButton(text3)
        self.button4 = QPushButton(text4)
        self.button5 = QPushButton(text5)

        self.connect(self.button1, SIGNAL("clicked()"), openFirstStory)
        self.connect(self.button2, SIGNAL("clicked()"), openSecondStory)
        self.connect(self.button3, SIGNAL("clicked()"), openThirdStory)
        self.connect(self.button4, SIGNAL("clicked()"), openForthStory)
        self.connect(self.button5, SIGNAL("clicked()"), openFifthStory)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)

        self.setLayout(layout)
        self.setWindowTitle("Trenutni naslovi na blic.rs")
        self.setWindowIcon(QIcon('blic.png'))


while True:
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
