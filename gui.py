import sys
import webbrowser
from PySide.QtCore import *
from PySide.QtGui import *
import storiesText
import hoveringText


def currentStoryOne():
    webbrowser.open(href1)


def currentStoryTwo():
    webbrowser.open(href2)


def currentStoryThree():
    webbrowser.open(href3)


def currentStoryFour():
    webbrowser.open(href4)


def currentStoryFive():
    webbrowser.open(href5)


def worldStoryOne():
    webbrowser.open(href10)


def worldStoryTwo():
    webbrowser.open(href11)


def worldStoryThree():
    webbrowser.open(href12)


def worldStoryFour():
    webbrowser.open(href13)


def chronicNewsOne():
    webbrowser.open(href14)


def chronicNewsTwo():
    webbrowser.open(href15)


def chronicNewsThree():
    webbrowser.open(href16)


def chronicNewsFour():
    webbrowser.open(href17)


def societyNewsOne():
    webbrowser.open(href18)


def societyNewsTWo():
    webbrowser.open(href19)


def societyNewsThree():
    webbrowser.open(href20)


def societyNewsFour():
    webbrowser.open(href21)


def economyNewsOne():
    webbrowser.open(href22)


def economyNewsTwo():
    webbrowser.open(href23)


def economyNewsThree():
    webbrowser.open(href24)


def economyNewsFour():
    webbrowser.open(href25)


text1, href1 = storiesText.firstHeadline()
text2, href2 = storiesText.secondHeadline()
text3, href3 = storiesText.thirdHeadline()
text4, href4 = storiesText.forthHeadline()
text5, href5 = storiesText.fifthHeadline()

hoveringText1 = hoveringText.hoverText1()
hoveringText2 = hoveringText.hoverText2()
hoveringText3 = hoveringText.hoverText3()
hoveringText4 = hoveringText.hoverText4()
hoveringText5 = hoveringText.hoverText5()

text10, href10 = storiesText.world_story_one()
text11, href11 = storiesText.world_story_one()
text12, href12 = storiesText.world_story_three()
text13, href13 = storiesText.world_story_four()

hoveringText6 = hoveringText.hoverText6()
hoveringText7 = hoveringText.hoverText7()
hoveringText8 = hoveringText.hoverText8()
hoveringText9 = hoveringText.hoverText9()

text14, href14 = storiesText.chronic_story_one()
text15, href15 = storiesText.chronic_story_two()
text16, href16 = storiesText.chronic_story_three()
text17, href17 = storiesText.chronic_story_four()

hoveringText10 = hoveringText.hoverText10()
hoveringText11 = hoveringText.hoverText11()
hoveringText12 = hoveringText.hoverText12()
hoveringText13 = hoveringText.hoverText13()

text18, href18 = storiesText.society_story_one()
text19, href19 = storiesText.society_story_two()
text20, href20 = storiesText.society_story_three()
text21, href21 = storiesText.society_story_four()

hoveringText14 = hoveringText.hoverText14()
hoveringText15 = hoveringText.hoverText15()
hoveringText16 = hoveringText.hoverText16()
hoveringText17 = hoveringText.hoverText17()


text22, href22 = storiesText.economy_story_one()
text23, href23 = storiesText.economy_story_two()
text24, href24 = storiesText.economy_story_three()
text25, href25 = storiesText.economy_story_four()


hoveringText18 = hoveringText.hoverText18()
hoveringText19 = hoveringText.hoverText19()
hoveringText20 = hoveringText.hoverText20()
hoveringText21 = hoveringText.hoverText21()


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.label1 = QLabel("<font color=#C11B17><b>" + 'Trenutne naslovne vesti:' + "</b></font>")
        self.label2 = QLabel("<font color=#C11B17><b>" + 'Svet:' + "</b></font>")
        self.label3 = QLabel("<font color=#C11B17><b>" + 'Hronika:' + "</b></font>")
        self.label4 = QLabel("<font color=#C11B17><b>" + 'Drustvo:' + "</b></font>")
        self.label5 = QLabel("<font color=#C11B17><b>" + 'Ekonomija:' + "</b></font>")

        button1 = QPushButton(text1, self)
        button1.setToolTip(hoveringText1)
        button2 = QPushButton(text2, self)
        button2.setToolTip(hoveringText2)
        button3 = QPushButton(text3, self)
        button3.setToolTip(hoveringText3)
        button4 = QPushButton(text4, self)
        button4.setToolTip(hoveringText4)
        button5 = QPushButton(text5, self)
        button5.setToolTip(hoveringText5)

        button6 = QPushButton(text10, self)
        button6.setToolTip(hoveringText6)
        button7 = QPushButton(text11, self)
        button7.setToolTip(hoveringText7)
        button8 = QPushButton(text12, self)
        button8.setToolTip(hoveringText8)
        button9 = QPushButton(text13, self)
        button9.setToolTip(hoveringText9)

        button10 = QPushButton(text14, self)
        button10.setToolTip(hoveringText10)
        button11 = QPushButton(text15, self)
        button11.setToolTip(hoveringText11)
        button12 = QPushButton(text16, self)
        button12.setToolTip(hoveringText12)
        button13 = QPushButton(text17, self)
        button13.setToolTip(hoveringText13)

        button14 = QPushButton(text18, self)
        button14.setToolTip(hoveringText14)
        button15 = QPushButton(text19, self)
        button15.setToolTip(hoveringText15)
        button16 = QPushButton(text20, self)
        button16.setToolTip(hoveringText16)
        button17 = QPushButton(text21, self)
        button17.setToolTip(hoveringText17)

        button18 = QPushButton(text22, self)
        button18.setToolTip(hoveringText18)
        button19 = QPushButton(text23, self)
        button19.setToolTip(hoveringText19)
        button20 = QPushButton(text24, self)
        button20.setToolTip(hoveringText20)
        button21 = QPushButton(text25, self)
        button21.setToolTip(hoveringText21)

        self.connect(button1, SIGNAL("clicked()"), currentStoryOne)
        self.connect(button2, SIGNAL("clicked()"), currentStoryTwo)
        self.connect(button3, SIGNAL("clicked()"), currentStoryThree)
        self.connect(button4, SIGNAL("clicked()"), currentStoryFour)
        self.connect(button5, SIGNAL("clicked()"), currentStoryFive)

        self.connect(button6, SIGNAL("clicked()"), worldStoryOne)
        self.connect(button7, SIGNAL("clicked()"), worldStoryTwo)
        self.connect(button8, SIGNAL("clicked()"), worldStoryThree)
        self.connect(button9, SIGNAL("clicked()"), worldStoryFour)

        self.connect(button10, SIGNAL("clicked()"), chronicNewsOne)
        self.connect(button11, SIGNAL("clicked()"), chronicNewsTwo)
        self.connect(button12, SIGNAL("clicked()"), chronicNewsThree)
        self.connect(button13, SIGNAL("clicked()"), chronicNewsFour)

        self.connect(button14, SIGNAL("clicked()"), societyNewsOne)
        self.connect(button15, SIGNAL("clicked()"), societyNewsTWo)
        self.connect(button16, SIGNAL("clicked()"), societyNewsThree)
        self.connect(button17, SIGNAL("clicked()"), societyNewsFour)

        self.connect(button18, SIGNAL("clicked()"), economyNewsOne)
        self.connect(button19, SIGNAL("clicked()"), economyNewsTwo)
        self.connect(button20, SIGNAL("clicked()"), economyNewsThree)
        self.connect(button21, SIGNAL("clicked()"), economyNewsFour)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        layout.addWidget(self.label2)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(button8)
        layout.addWidget(button9)

        layout.addWidget(self.label3)
        layout.addWidget(button10)
        layout.addWidget(button11)
        layout.addWidget(button12)
        layout.addWidget(button13)

        layout.addWidget(self.label4)
        layout.addWidget(button14)
        layout.addWidget(button15)
        layout.addWidget(button16)
        layout.addWidget(button17)

        layout.addWidget(self.label5)
        layout.addWidget(button18)
        layout.addWidget(button19)
        layout.addWidget(button20)
        layout.addWidget(button21)

        self.setLayout(layout)
        self.setWindowTitle("Naslovi na blic.rs")
        self.setWindowIcon(QIcon('blic.png'))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
