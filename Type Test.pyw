from secrets import choice
import sys
import os
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import*
from PyQt5.QtWidgets import QMessageBox
import random

values = []
wordlist = []
words = []
chars = []
enter_word_chars = []


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.flag = False
        self.time = 0.0
        self.sayaç = 0
        self.doğru = 0
        self.yanlış = 0

        # Fill
        self.fill_login = QtWidgets.QLabel(self)
        self.fill_login.resize(1000, 1000)
        self.fill_login.move(-10, -10)
        self.fill_login.setStyleSheet("background-color : rgb(130,240,226)")

        # Title
        self.title = QtWidgets.QLabel(self)
        self.title.move(350, 5)
        self.title.setFont(QtGui.QFont("Helvetica", 40))
        self.title.setText("TYPE TEST")

        # Random Words
        self.random_words = QtWidgets.QTextEdit(self)
        self.random_words.resize(800, 150)
        self.random_words.move(50, 80)
        self.random_words.setFont(QtGui.QFont("Helvetica", 20))
        self.random_words.setReadOnly(True)

        # Word
        self.word = QtWidgets.QLabel(self)
        self.word.setText("Waiting...")
        self.word.setFont(QtGui.QFont("Helvetica", 30))
        self.word.setStyleSheet("color : white")
        self.word.move(550, 330)
        self.word.resize(290, 50)

        # clock
        font = QtGui.QFont("Open Sans", 70, QtGui.QFont.Bold)
        self.clock = QtWidgets.QLabel(self)
        self.clock.setFont(font)
        self.clock.move(455, 390)
        self.clock.resize(500, 90)

        # Enter
        self.enter_word = QtWidgets.QLineEdit(self)
        self.enter_word.keyPressEvent = self._keyPressEvent
        self.enter_word.resize(725, 50)
        self.enter_word.move(50, 250)
        self.enter_word.setFont(QtGui.QFont("Helvetica", 15))
        self.enter_word.setReadOnly(True)
        self.enter_word.setPlaceholderText("Space to pass...")

        # Start Button
        self.start = QtWidgets.QPushButton(self)
        self.start.resize(50, 50)
        self.start.move(800, 250)
        self.start.setText("GO!")
        self.start.setFont(QtGui.QFont("Helvetica", 15))
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Results Main
        self.results = QtWidgets.QLabel(self)
        self.results.move(50, 365)
        self.results.resize(250, 100)
        self.results.setText("   0 WPM")
        self.results.setFont(QtGui.QFont("Helvetica", 30))

        # Results Title
        myFont = QtGui.QFont("Helvetica")
        myFont.setBold(True)
        self.results_title = QtWidgets.QLabel(self)
        self.results_title.setText("RESULTS :")
        self.results_title.move(50, 336)
        self.results_title.resize(250, 30)
        self.results_title.setFont(QtGui.QFont("Helvetica", 15))

        # Results True
        self.results_true = QtWidgets.QLabel(self)
        self.results_true.resize(250, 40)
        self.results_true.move(50, 489)
        self.results_true.setText("""Correct Words:""")
        self.results_true.setFont(QtGui.QFont("Helvetica", 15))

        # Results Wrong
        self.results_wrong = QtWidgets.QLabel(self)
        self.results_wrong.resize(250, 40)
        self.results_wrong.move(50, 450)
        self.results_wrong.setText("Wrong Words:")
        self.results_wrong.setFont(QtGui.QFont("Helvetica", 15))

        # Back button
        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.move(720, 520)
        self.back_button.resize(130, 50)
        self.back_button.setText("Back!")
        self.back_button.setFont(QtGui.QFont("Helvetica", 15))
        self.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Best
        self.best = QtWidgets.QLabel(self)
        self.best.setText("Best:")
        self.best.setFont(QtGui.QFont("Heşvetica", 15))
        self.best.move(50, 528)
        self.best.resize(250, 40)

        # Try Again
        self.try_again = QtWidgets.QPushButton(self)
        self.try_again.move(570, 520)
        self.try_again.resize(130, 50)
        self.try_again.setText("Try Again!")
        self.try_again.setFont(QtGui.QFont("Helvetica", 15))
        self.try_again.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Settings
        self.settings = QtWidgets.QPushButton(self)
        self.settings.move(420, 520)
        self.settings.resize(130, 50)
        self.settings.setText("Settings")
        self.settings.setFont(QtGui.QFont("Helvetica", 15))
        self.settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.stopwatch)
        self.timer.start(100)

        self.settings.clicked.connect(self.settings_func)
        self.start.clicked.connect(self.start_func)
        self.try_again.clicked.connect(self.try_again_func)
        self.back_button.clicked.connect(self.previous)

        with open("Data\\values.TXT", "r", encoding="utf-8")as file:
            a = file.readline()
            if a == "1":
                self.start.setStyleSheet(
                    "background-color : black; color : white ; border: 2px solid rgb(67,255,0);")
                self.back_button.setStyleSheet(
                    "background-color : black; color : white ; border: 2px solid rgb(67,255,0);")
                self.settings.setStyleSheet(
                    "background-color : black; color : white ; border: 2px solid rgb(67,255,0);")
                self.try_again.setStyleSheet(
                    "background-color : black; color : white ; border: 2px solid rgb(67,255,0);")
                self.random_words.setStyleSheet(
                    "border: 2px solid rgb(67,255,0);color : white")
                self.enter_word.setStyleSheet(
                    "border: 2px solid rgb(67,255,0); color : rgb(255,255,255)")
                self.results_wrong.setStyleSheet(
                    "border: 2px solid rgb(67,255,0); color : red")
                self.best.setStyleSheet(
                    "border: 2px solid rgb(67,255,0); color : yellow")
                self.results_title.setStyleSheet(
                    "border: 2px solid rgb(67,255,0); color : blue")
                self.results_true.setStyleSheet(
                    "border: 2px solid rgb(67,255,0);color: green")
                self.results.setStyleSheet(
                    "border: 2px solid rgb(67,255,0);color: rgb(255,255,255)")
                self.title.setStyleSheet("color: rgb(255,255,255)")
                self.setStyleSheet("background-color : black")
                self.clock.setStyleSheet("color : red")
                self.fill_login.setStyleSheet("background-color : black")
            if a == "0":
                self.settings.setStyleSheet(
                    "background-color : rgb(223,108,29); color : rgb(243,184,144);")
                self.best.setStyleSheet(
                    "background-color : rgb(200,200,200); border: 1px solid black")
                self.back_button.setStyleSheet(
                    "background-color : rgb(223,108,29); color : rgb(243,184,144);")
                self.setStyleSheet("background-color : rgb(178,240,226)")
                self.try_again.setStyleSheet(
                    "background-color : rgb(223,108,29); color : rgb(243,184,144);")
                self.results_wrong.setStyleSheet(
                    "background-color : rgb(200,200,200); border: 1px solid black")
                self.results_true.setStyleSheet(
                    "background-color : rgb(255,255,255); border: 1px solid black")
                self.results_title.setStyleSheet(
                    "background-color : rgb(200,200,200); border: 1px solid black")
                self.results.setStyleSheet(
                    "background-color : rgb(255,255,255); border: 1px solid black;")
                self.start.setStyleSheet(
                    "background-color : rgb(223,108,29); color : rgb(243,184,144)")
                self.enter_word.setStyleSheet("border: 2px solid black;"
                                              "background-color : rgb(255,255,255)")
                self.random_words.setStyleSheet("border: 2px solid black;"
                                                "background-color : rgb(255,255,255)")
                self.title.setStyleSheet("color : rgb(0,0,0)")
                self.title.setStyleSheet("color : rgb(0,0,0)")
                self.fill_login.setStyleSheet(
                    "background-color : rgb(178,240,226)")
                self.clock.setStyleSheet("color : black")

    def previous(self):
        stack.setCurrentIndex(stack.currentIndex() - 1)

    def stopwatch(self):
        if self.flag:
            self.time += 1
        self.clock.setText(str(self.time/10))

    def start_func(self):
        print(values)
        print(words)
        self.flag = True
        self.random_words.setReadOnly(True)
        self.enter_word.setReadOnly(False)
        self.start.setDisabled(True)

        if values[0] == "0":  # if random
            try:
                if values[2] == "1":
                    with open("Data\\easy.TXT", "r+", encoding="utf-8")as easy_file:
                        wordlist.append(easy_file.readlines())
                        for i in range(int(values[1])):
                            word_order = random.randint(0, 2500)
                            regulator = []
                            list_word = ""
                            for chars in wordlist[0][word_order]:
                                regulator.append(chars)
                            regulator.pop()
                            for char in regulator:
                                list_word += char
                            words.append(list_word)
                            print(words)
                            list_word = ""
                            self.word.setText(words[self.sayaç])
                    for word in words:
                        self.random_words.setText(
                            self.random_words.toPlainText() + word + " ")

                if values[2] == "2":
                    with open("Data\\normal.TXT", "r+", encoding="utf-8")as normal_file:
                        wordlist.append(normal_file.readlines())
                        for i in range(int(values[1])):
                            word_order = random.randint(0, 3500)
                            regulator = []
                            list_word = ""
                            for chars in wordlist[0][word_order]:
                                regulator.append(chars)
                            regulator.pop()
                            for char in regulator:
                                list_word += char
                            words.append(list_word)
                            list_word = ""
                            self.word.setText(words[self.sayaç])
                    for word in words:
                        self.random_words.setText(
                            self.random_words.toPlainText() + word + " ")

                if values[2] == "3":
                    with open("Data\\hard.TXT", "r+", encoding="utf-8")as hard_file:
                        wordlist.append(hard_file.readlines())
                        for i in range(int(values[1])):
                            word_order = random.randint(0, 1351)
                            regulator = []
                            list_word = ""
                            for chars in wordlist[0][word_order]:
                                regulator.append(chars)
                            regulator.pop()
                            for char in regulator:
                                list_word += char
                            words.append(list_word)
                            list_word = ""
                            self.word.setText(words[self.sayaç])
                    for word in words:
                        self.random_words.setText(
                            self.random_words.toPlainText() + word + " ")

                if values[2] == "4":
                    with open("Data\\mixed.TXT", "r+", encoding="utf-8")as mixed_file:
                        wordlist.append(mixed_file.readlines())
                        for i in range(int(values[1])):
                            word_order = random.randint(0, 7397)
                            regulator = []
                            list_word = ""
                            for chars in wordlist[0][word_order]:
                                regulator.append(chars)
                            regulator.pop()
                            for char in regulator:
                                list_word += char
                            words.append(list_word)
                            list_word = ""
                            self.word.setText(words[self.sayaç])
                    for word in words:
                        self.random_words.setText(
                            self.random_words.toPlainText() + word + " ")
            except ValueError:
                pass

        if values[0] == "1":
            for p in words:
                self.random_words.setText(
                    self.random_words.toPlainText() + p + " ")
                print(self.sayaç, "Sayaçç")
                self.word.setText(words[self.sayaç])

    def try_again_func(self):
        self.flag = False
        self.time = 0
        self.enter_word.setReadOnly(False)
        values.clear()
        print(values)
        self.word.setText("Waiting...")
        stack.setCurrentIndex(stack.currentIndex() - 1)
        self.results.setText("    0 WPM")
        self.results_true.setText("Correct Words")
        self.results_wrong.setText("Wrong Words")
        self.random_words.setText("")
        self.sayaç = 0
        self.doğru = 0
        self.yanlış = 0
        wordlist.clear()
        words.clear()
        self.start.setEnabled(True)

    def settings_func(self):
        setting_message = QMessageBox()
        setting_message.setWindowTitle("Settings")
        setting_message.setWindowIcon(QtGui.QIcon("Settings-icon.png"))
        setting_message.setStyleSheet(
            "QLabel{min-width: 200px; min-height: 200px}")
        self.save_button = QtWidgets.QPushButton(setting_message)
        self.save_button.setText("Save")
        self.save_button.resize(80, 23)
        self.save_button.move(70, 232)
        self.msg_title = QtWidgets.QLabel(setting_message)
        self.msg_title.move(60, -90)
        self.msg_title.setText("APPEARANCE")
        self.msg_title.setFont(QtGui.QFont("Helvetica", 15))
        self.light_blue = QtWidgets.QRadioButton(setting_message)
        self.light_blue.setText("Light Blue")
        self.light_blue.move(20, 60)
        self.high_contrast = QtWidgets.QRadioButton(setting_message)
        self.high_contrast.setText("High Contrast")
        self.high_contrast.move(20, 40)
        self.save_button.clicked.connect(lambda: self.set_appearance(
            self.high_contrast.isChecked(), self.light_blue.isChecked(),))
        p = setting_message.exec_()

    def set_appearance(self, high_contrast, light_blue):
        if high_contrast:
            with open("Data\\values.TXT", "r+", encoding="utf-8")as file:
                file.write("1")
            self.start.setStyleSheet(
                "background-color : black; color : white ; border: 2px solid rgb(67,255,0);")
            self.back_button.setStyleSheet(
                "background-color : black; color : white ; border: 2px solid rgb(67,255,0);")
            self.settings.setStyleSheet(
                "background-color : black; color : white ; border: 2px solid rgb(67,255,0);")
            self.try_again.setStyleSheet(
                "background-color : black; color : white ; border: 2px solid rgb(67,255,0);")
            self.random_words.setStyleSheet(
                "border: 2px solid rgb(67,255,0);color : white")
            self.enter_word.setStyleSheet(
                "border: 2px solid rgb(67,255,0); color : rgb(255,255,255)")
            self.results_wrong.setStyleSheet(
                "border: 2px solid rgb(67,255,0); color : red")
            self.best.setStyleSheet(
                "border: 2px solid rgb(67,255,0); color : yellow")
            self.results_title.setStyleSheet(
                "border: 2px solid rgb(67,255,0); color : blue")
            self.results_true.setStyleSheet(
                "border: 2px solid rgb(67,255,0);color: green")
            self.results.setStyleSheet(
                "border: 2px solid rgb(67,255,0);color: rgb(255,255,255)")
            self.title.setStyleSheet("color: rgb(255,255,255)")
            self.setStyleSheet("background-color : black")
            self.clock.setStyleSheet("color : red")
            self.fill_login.setStyleSheet("background-color : black")

        if light_blue:
            with open("Data\\values.TXT", "r+", encoding="utf-8")as file:
                file.write("0")
            self.settings.setStyleSheet(
                "background-color : rgb(223,108,29); color : rgb(243,184,144);")
            self.best.setStyleSheet(
                "background-color : rgb(200,200,200); border: 1px solid black")
            self.back_button.setStyleSheet(
                "background-color : rgb(223,108,29); color : rgb(243,184,144);")
            self.setStyleSheet("background-color : rgb(178,240,226)")
            self.try_again.setStyleSheet(
                "background-color : rgb(223,108,29); color : rgb(243,184,144);")
            self.results_wrong.setStyleSheet(
                "background-color : rgb(200,200,200); border: 1px solid black")
            self.results_true.setStyleSheet(
                "background-color : rgb(255,255,255); border: 1px solid black")
            self.results_title.setStyleSheet(
                "background-color : rgb(200,200,200); border: 1px solid black")
            self.results.setStyleSheet(
                "background-color : rgb(255,255,255); border: 1px solid black;")
            self.start.setStyleSheet(
                "background-color : rgb(223,108,29); color : rgb(243,184,144)")
            self.enter_word.setStyleSheet("border: 2px solid black;"
                                          "background-color : rgb(255,255,255)")
            self.random_words.setStyleSheet("border: 2px solid black;"
                                            "background-color : rgb(255,255,255)")
            self.title.setStyleSheet("color : rgb(0,0,0)")
            self.title.setStyleSheet("color : rgb(0,0,0)")
            self.fill_login.setStyleSheet(
                "background-color : rgb(178,240,226)")
            self.clock.setStyleSheet("color : black")

    def _keyPressEvent(self, event: QtGui.QKeyEvent):
        try:
            key = event.text()
            if event.key() == QtCore.Qt.Key.Key_Backspace:
                chars = []
                for i in self.enter_word.text():
                    chars.append(i)
                self.enter_word.clear()
                chars.pop()
                for char in chars:
                    self.enter_word.setText(self.enter_word.text() + char)
                self.word_listener()
            if key == " ":
                self.check_2()
                self.enter_word.clear()
                chars = []
                for i in self.enter_word.text():
                    chars.append(i)
                self.enter_word.clear()
                chars.pop()
                for char in chars:
                    self.enter_word.setText(self.enter_word.text() + char)
            if not key.isprintable():
                return
            self.enter_word.setText(self.enter_word.text() + key)
            self.word_listener()
        except IndexError:
           pass

                

    def check_2(self):
        try:
            for word in words:
                if self.enter_word.text() == words[self.sayaç]:
                    self.sayaç += 1
                    self.doğru += 1
                    self.word.setText(words[self.sayaç])
                    print("True", self.doğru, self.sayaç, "Sayaççç")
                    break
                if self.enter_word.text() != words[self.sayaç]:
                    self.sayaç += 1
                    self.yanlış += 1
                    self.word.setText(words[self.sayaç])
                    print("False", self.yanlış, self.sayaç, "Sayaççç")
                    break
        except IndexError:
            self.check_sayaç()

    def check_sayaç(self):
        if self.sayaç == int(values[1]):
            self.give_results()
        else:
            pass

    def word_listener(self):
        for i in self.enter_word.text():
            enter_word_chars.append(i)
            print(enter_word_chars)
        for p in words[self.sayaç]:
            chars.append(p)
        self.check()
        chars.clear()
        enter_word_chars.clear()

    def check(self):
        for i in range(0, len(self.enter_word.text())):
            print(i)
            if chars[i] == enter_word_chars[i]:
                self.word.setStyleSheet("color : green")
            else:
                self.word.setStyleSheet("color : red")
                break

    def give_results(self):
        self.minute = (self.time/10)/60
        print(self.minute)
        self.flag = False
        self.enter_word.setReadOnly(True)
        self.word.setText("Finished!")
        self.enter_word.setReadOnly(True)
        self.results_wrong.setText("Wrong Words: {}".format(self.yanlış))
        self.results_true.setText("Correct Words: {}".format(self.doğru))
        self.results.setText("{} WPM".format(round(self.doğru/self.minute, 1)))


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # Window
        width = 900
        height = 600

        # fill
        self.fill = QtWidgets.QLabel(self)
        self.fill.setStyleSheet("background-color : rgb(178,240,226)")
        self.fill.resize(1000, 1000)
        self.fill.move(-10, -10)

        # Level
        self.easy = QtWidgets.QRadioButton(self)
        self.easy.setText("EASY")
        self.easy.move(20, 220)
        self.normal = QtWidgets.QRadioButton(self)
        self.normal.setText("NORMAL")
        self.normal.move(85, 220)
        self.hard = QtWidgets.QRadioButton(self)
        self.hard.setText("HARD")
        self.hard.move(165, 220)

        # Title
        self.title = QtWidgets.QLabel(self)
        self.title.move(350, 15)
        self.title.setStyleSheet("color : rgb(0,0,0)")
        self.title.setFont(QtGui.QFont("Helvetica", 35))
        self.title.setText("TYPE TEST")

        # Mark 1
        self.mark_1 = QtWidgets.QLabel(self)
        self.mark_1.move(400, 80)
        self.mark_1.resize(70, 40)

        # Mark 2
        self.mark_2 = QtWidgets.QLabel(self)
        self.mark_2.move(320, 270)
        self.mark_2.resize(70, 40)

        # chocie 1
        self.chocie_1 = QtWidgets.QCheckBox(self)
        self.chocie_1.move(20, 90)

        # How Many Box
        self.how_many_word = QtWidgets.QLineEdit(self)
        self.how_many_word.move(140, 155)
        self.how_many_word.resize(80, 40)
        self.how_many_word.setStyleSheet("background : rgb(222,237,241)")
        self.how_many_word.setValidator(QtGui.QDoubleValidator())
        self.how_many_word.setFont(QtGui.QFont("Helvetica", 12))
        self.how_many_word.setMaxLength(3)

        # How many label
        self.how_many_label = QtWidgets.QLabel(self)
        self.how_many_label.setText("How many : ")
        self.how_many_label.setFont(QtGui.QFont("Helvetica", 15))
        self.how_many_label.move(20, 160)

        # chocie 2
        self.chocie_2 = QtWidgets.QCheckBox(self)
        self.chocie_2.move(20, 275)

        # Choice 2 QLineEdit
        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.move(20, 330)
        self.text_edit.resize(375, 250)
        self.text_edit.setStyleSheet("background : rgb(222,237,241)")
        self.text_edit.setPlaceholderText("Type Here...")

        # Chocie Buttons
        self.chocie_1_button = QtWidgets.QPushButton(self)
        self.chocie_1_button.move(19, 84)
        self.chocie_1_button.resize(30, 30)
        self.chocie_1_button.setStyleSheet(
            "background-color : rgb(150,150,150)")
        self.chocie_1_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.chocie_2_button = QtWidgets.QPushButton(self)
        self.chocie_2_button.move(19, 274)
        self.chocie_2_button.resize(30, 30)
        self.chocie_2_button.setStyleSheet(
            "background-color : rgb(150,150,150)")
        self.chocie_2_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Labels of Chocies
        self.chocie_1_label = QtWidgets.QLabel(self)
        self.chocie_1_label.setText("I want my words randomly")
        self.chocie_1_label.move(65, 82)
        self.chocie_1_label.setFont(QtGui.QFont("Helvetica font", 20))

        self.chocie_2_label = QtWidgets.QLabel(self)
        self.chocie_2_label.setText("I will give the words")
        self.chocie_2_label.move(65, 272)
        self.chocie_2_label.setFont(QtGui.QFont("Helvetica font", 20))

        # Settings
        self.settings_login = QtWidgets.QPushButton(self)
        self.settings_login.move(530, 520)
        self.settings_login.resize(130, 50)
        self.settings_login.setText("Settings")
        self.settings_login.setStyleSheet(
            "background-color : rgb(223,108,29); color : rgb(243,184,144);")
        self.settings_login.setFont(QtGui.QFont("Helvetica", 15))
        self.settings_login.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # How To Use Label
        self.How_To_Use = QtWidgets.QLabel(self)
        self.How_To_Use.setText(""" 
Type test is an application that 
shows how fast you type on the 
keyboard. Before starting the 
test, the user is presented with 
2 options and comes across as many 
words as the selected word count.
If you choose option 2, you can 
write the words yourself. But if 
you choose option 1, the words 
will appear randomly in front of 
you. After you choose how many 
words you want, the words will 
begin to appear in front of you. 
              Have fun :)      
        """)
        self.How_To_Use.setFont(QtGui.QFont("Helvetica", 15))
        self.How_To_Use.setStyleSheet("color : rgb(16,14,14)")
        self.How_To_Use.move(530, 110)

        # how to use label 2
        self.How_To_Use_2 = QtWidgets.QLabel(self)
        self.How_To_Use_2.setText("How To Use")
        self.How_To_Use_2.move(530, 100)
        self.How_To_Use_2.setStyleSheet("color : rgb(0,27,51)")
        self.How_To_Use_2.setFont(QtGui.QFont("Helvetica", 15))

        # Start Button
        self.start_button = QtWidgets.QPushButton(self)
        self.start_button.move(690, 520)
        self.start_button.resize(170, 50)
        self.start_button.setText("Start Typing Test!")
        self.start_button.setStyleSheet(
            "background-color : rgb(223,108,29); color : rgb(243,184,144)")
        self.start_button.setFont(QtGui.QFont("Helvetica", 15))
        self.start_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # linking Buttons to the Functions
        self.chocie_2_button.clicked.connect(self.chocie_1_checking)
        self.chocie_1.stateChanged.connect(self.marking_1)

        self.chocie_1_button.clicked.connect(self.chocie_2_checking)
        self.chocie_2.stateChanged.connect(self.marking_2)

        self.start_button.clicked.connect(self.start)

        self.settings_login.clicked.connect(self.settings_login_func)

        with open("Data\\values.TXT", "r+", encoding="utf-8")as file:
            a = file.readline()
            if a == "1":
                self.title.setStyleSheet("color : white")
                self.setStyleSheet("background-color : black")
                self.how_many_label.setStyleSheet("color : white")
                self.How_To_Use.setStyleSheet("color : white")
                self.How_To_Use_2.setStyleSheet("color : yellow")
                self.chocie_1_label.setStyleSheet("color : white")
                self.start_button.setStyleSheet(
                    "color : white; border : 2px solid rgb(67,255,0);")
                self.settings_login.setStyleSheet(
                    "color : white; border : 2px solid rgb(67,255,0)")
                self.how_many_word.setStyleSheet(
                    "color : white;border : 2px solid rgb(67,255,0)")
                self.chocie_2_label.setStyleSheet("color : white")
                self.text_edit.setStyleSheet(
                    "color : white;border: 2px solid rgb(67,255,0)")
                self.easy.setStyleSheet("color : red")
                self.normal.setStyleSheet("color : red")
                self.hard.setStyleSheet("color : red")
                self.fill.setStyleSheet("background-color : black")

            if a == "0":
                self.chocie_1_label.setStyleSheet("color : rgb(0,0,0)")
                self.chocie_2_label.setStyleSheet("color : rgb(0,0,0)")
                self.how_many_label.setStyleSheet("color : rgb(0,0,0)")
                self.start_button.setStyleSheet(
                    "background-color : rgb(223,108,29); color : rgb(243,184,144)")
                self.How_To_Use_2.setStyleSheet("color : rgb(0,27,51)")
                self.How_To_Use.setStyleSheet("color : rgb(16,14,14)")
                self.settings_login.setStyleSheet(
                    "background-color : rgb(223,108,29); color : rgb(243,184,144);")
                self.chocie_2_button.setStyleSheet(
                    "background-color : rgb(150,150,150)")
                self.chocie_1_button.setStyleSheet(
                    "background-color : rgb(150,150,150)")
                self.text_edit.setStyleSheet("background : rgb(222,237,241)")
                self.title.setStyleSheet("color : rgb(0,0,0)")
                self.setStyleSheet("background-color : rgb(178,240,226)")
                self.how_many_word.setStyleSheet(
                    "background : rgb(222,237,241)")
                self.hard.setStyleSheet("color : black")
                self.easy.setStyleSheet("color : black")
                self.normal.setStyleSheet("color : black")
                self.fill.setStyleSheet("background-color : rgb(178,240,226)")

    def settings_login_func(self):
        setting_message_login = QMessageBox()
        setting_message_login.setWindowTitle("Settings")
        setting_message_login.setWindowIcon(QtGui.QIcon("Settings-icon.png"))
        setting_message_login.setStandardButtons(QMessageBox.Ok)
        setting_message_login.setStyleSheet(
            "QLabel{min-width: 200px; min-height: 200px}")
        self.save_button_login = QtWidgets.QPushButton(setting_message_login)
        self.save_button_login.setText("Save")
        self.save_button_login.resize(80, 23)
        self.save_button_login.move(70, 232)
        self.title_login = QtWidgets.QLabel(setting_message_login)
        self.title_login.move(60, -90)
        self.title_login.setText("APPEARANCE")
        self.title_login.setFont(QtGui.QFont("Helvetica", 15))
        self.light_blue_login = QtWidgets.QRadioButton(setting_message_login)
        self.light_blue_login.setText("Light Blue")
        self.light_blue_login.move(20, 60)
        self.high_contrast_login = QtWidgets.QRadioButton(
            setting_message_login)
        self.high_contrast_login.setText("High Contrast")
        self.high_contrast_login.move(20, 40)
        self.save_button_login.clicked.connect(lambda: self.set_appearance_login(
            self.high_contrast_login.isChecked(), self.light_blue_login.isChecked()))
        p = setting_message_login.exec_()

    def set_appearance_login(self, high_contrast_login, light_blue_login):
        if high_contrast_login:
            with open("Data\\values.TXT", "r+", encoding="utf-8")as file:
                file.write("1")
            self.title.setStyleSheet("color : white")
            self.setStyleSheet("background-color : black")
            self.how_many_label.setStyleSheet("color : white")
            self.How_To_Use.setStyleSheet("color : white")
            self.How_To_Use_2.setStyleSheet("color : yellow")
            self.chocie_1_label.setStyleSheet("color : white")
            self.start_button.setStyleSheet(
                "color : white; border : 2px solid rgb(67,255,0)")
            self.settings_login.setStyleSheet(
                "color : white; border : 2px solid rgb(67,255,0)")
            self.how_many_word.setStyleSheet(
                "color : white;border : 2px solid rgb(67,255,0)")
            self.chocie_2_label.setStyleSheet("color : white")
            self.text_edit.setStyleSheet(
                "color : white;border: 2px solid rgb(67,255,0)")
            self.easy.setStyleSheet("color : red")
            self.normal.setStyleSheet("color : red")
            self.hard.setStyleSheet("color : red")
            self.fill.setStyleSheet("background-color : black")

        if light_blue_login:
            with open("Data\\values.TXT", "r+", encoding="utf-8")as file:
                file.write("0")
            self.chocie_1_label.setStyleSheet("color : rgb(0,0,0)")
            self.chocie_2_label.setStyleSheet("color : rgb(0,0,0)")
            self.how_many_label.setStyleSheet("color : rgb(0,0,0)")
            self.start_button.setStyleSheet(
                "background-color : rgb(223,108,29); color : rgb(243,184,144)")
            self.How_To_Use_2.setStyleSheet("color : rgb(0,27,51)")
            self.How_To_Use.setStyleSheet("color : rgb(16,14,14)")
            self.settings_login.setStyleSheet(
                "background-color : rgb(223,108,29); color : rgb(243,184,144);")
            self.chocie_2_button.setStyleSheet(
                "background-color : rgb(150,150,150)")
            self.chocie_1_button.setStyleSheet(
                "background-color : rgb(150,150,150)")
            self.text_edit.setStyleSheet("background : rgb(222,237,241)")
            self.title.setStyleSheet("color : rgb(0,0,0)")
            self.setStyleSheet("background-color : rgb(178,240,226)")
            self.how_many_word.setStyleSheet("background : rgb(222,237,241)")
            self.hard.setStyleSheet("color : black")
            self.easy.setStyleSheet("color : black")
            self.normal.setStyleSheet("color : black")
            self.fill.setStyleSheet("background-color : rgb(178,240,226)")

    def start(self):
        wrong_characters = ["+", "-", "e", "E", ","]
        if self.chocie_1.isChecked() or self.chocie_2.isChecked():
            pass
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Please choose one of the options.")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon("Assets\\error.png"))
            x = msg.exec_()
        if self.chocie_1.isChecked():
            error_number = 0
            if self.how_many_word.text():
                for i in self.how_many_word.text():
                    if i in wrong_characters:
                        error_number += 1
                    else:
                        pass
                if error_number > 0:
                    msg2 = QMessageBox()
                    msg2.setWindowTitle("Warning")
                    msg2.setText("Please enter numbers only.")
                    msg2.setIcon(QMessageBox.Critical)
                    msg2.setWindowIcon(QtGui.QIcon("Assets\\error.png"))
                    y = msg2.exec_()
                if error_number == 0:
                    values.append("0")
                    values.append(self.how_many_word.text())
                    if self.hard.isChecked():
                        values.append("3")
                    if self.normal.isChecked():
                        values.append("2")
                    if self.easy.isChecked():
                        values.append("1")
                    if self.easy.isChecked() == False and self.normal.isChecked() == False and self.hard.isChecked() == False:
                        values.append("4")
                    stack.setCurrentIndex(stack.currentIndex() + 1)
            else:
                msg3 = QMessageBox()
                msg3.setWindowTitle("Warning")
                msg3.setText("Enter how many words you want.")
                msg3.setIcon(QMessageBox.Question)
                msg3.setWindowIcon(QtGui.QIcon("Assets\\error.png"))
                z = msg3.exec_()

        if self.chocie_2.isChecked():
            if self.text_edit.toPlainText():
                values.append("1")
                words.extend(self.text_edit.toPlainText().split())
                print(words)
                values.append(len(words))
                stack.setCurrentIndex(stack.currentIndex() + 1)
                

            else:
                msg4 = QMessageBox()
                msg4.setWindowTitle("Warning")
                msg4.setText("Enter a few words.             ")
                msg4.setIcon(QMessageBox.Question)
                msg4.setWindowIcon(QtGui.QIcon("Assets\\error.png"))
                p = msg4.exec_()

    def chocie_1_checking(self):
        if self.chocie_2.isChecked():
            self.chocie_2.setChecked(False)
        else:
            self.chocie_2.setChecked(True)
            self.chocie_1.setChecked(False)

    def chocie_2_checking(self):
        if self.chocie_1.isChecked():
            self.chocie_1.setChecked(False)
        else:
            self.chocie_1.setChecked(True)
            self.chocie_2.setChecked(False)

    def marking_1(self):
        if self.chocie_1.isChecked() == False:
            self.mark_1.clear()
        if self.chocie_1.isChecked():
            self.mark_1.setPixmap(QtGui.QPixmap("Assets\\Ok.png"))

    def marking_2(self):
        if self.chocie_2.isChecked():
            self.mark_2.setPixmap(QtGui.QPixmap("Assets\\Ok.png"))
        if self.chocie_2.isChecked() == False:
            self.mark_2.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    stack = QtWidgets.QStackedWidget()
    login = Window()
    test = MainWindow()
    stack.addWidget(login)
    stack.addWidget(test)
    stack.setFixedSize(900, 600)
    stack.setWindowTitle("Type Test")
    stack.setWindowIcon(QtGui.QIcon("Assets\\icon.png"))
    stack.show()
    sys.exit(app.exec_())
