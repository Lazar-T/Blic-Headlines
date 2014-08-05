import sys
import webbrowser
from PySide.QtCore import *
from PySide.QtGui import *
import scrapingBlic
import worldNews
import chronicNews
import societyNews
import economyNews
from hoveringText import headlinesHover, worldNewsHover, chronicNewsHover, societyNewsHover, economyNewsHover


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


text1, href1 = scrapingBlic.firstHeadline()
text2, href2 = scrapingBlic.secondHeadline()
text3, href3 = scrapingBlic.thirdHeadline()
text4, href4 = scrapingBlic.forthHeadline()
text5, href5 = scrapingBlic.fifthHeadline()

hoveringText1 = headlinesHover.hoverText1()
hoveringText2 = headlinesHover.hoverText2()
hoveringText3 = headlinesHover.hoverText3()
hoveringText4 = headlinesHover.hoverText4()
hoveringText5 = headlinesHover.hoverText5()

text10, href10 = worldNews.worldNewsOne()
text11, href11 = worldNews.worldNewsTwo()
text12, href12 = worldNews.worldNewsThree()
text13, href13 = worldNews.worldNewsFour()

hoveringText6 = worldNewsHover.hoverText6()
hoveringText7 = worldNewsHover.hoverText7()
hoveringText8 = worldNewsHover.hoverText8()
hoveringText9 = worldNewsHover.hoverText9()

text14, href14 = chronicNews.chronicStoryOne()
text15, href15 = chronicNews.chronicStoryTwo()
text16, href16 = chronicNews.chronicStoryThree()
text17, href17 = chronicNews.chronicStoryFour()

hoveringText10 = chronicNewsHover.hoverText10()
hoveringText11 = chronicNewsHover.hoverText11()
hoveringText12 = chronicNewsHover.hoverText12()
hoveringText13 = chronicNewsHover.hoverText13()

text18, href18 = societyNews.societyStoryOne()
text19, href19 = societyNews.societyStoryTwo()
text20, href20 = societyNews.societyStoryThree()
text21, href21 = societyNews.societyStoryFour()

hoveringText14 = societyNewsHover.hoverText14()
hoveringText15 = societyNewsHover.hoverText15()
hoveringText16 = societyNewsHover.hoverText16()
hoveringText17 = societyNewsHover.hoverText17()


text22, href22 = economyNews.economyStoryOne()
text23, href23 = economyNews.economyStoryTwo()
text24, href24 = economyNews.economyStoryThree()
text25, href25 = economyNews.economyStoryFour()


hoveringText18 = economyNewsHover.hoverText18()
hoveringText19 = economyNewsHover.hoverText19()
hoveringText20 = economyNewsHover.hoverText20()
hoveringText21 = economyNewsHover.hoverText21()


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
        #button4.setToolTip(hoveringText4)
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
