import string
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QTextCursor


class Message(object):
    start = '智力竞赛现在开始!\n'
    success = '聪明伶俐一百分!\n'
    fail1 = '真可惜,您在本次竞赛中挑战失败,请继续努力!\n'
    fail2 = '本次题目的答案是{}'
    alert = '输入数字非法, 请输入4位不重复的数字.'
    title_help = '游戏帮助'
    help = '''1.游戏开始,计算机将随机产生一个各位数字不重复的四位数.

2.请将您猜的数填在输入框内按回车或"提交"按钮提交.

3.当获得合法的输入数字后,计算机会将您提交的数与它刚才生成的数进行比较,并通过"历史记录"框输出比较结果,比较结果以"?A?B"的形式显示.A表示位置和数字均正确,B表示数字正确但位置不正确.比如:"2A1B"表示您已经将2个正确的数字填入了正确的位置,但还有一个数字是正确的,只是填错了位置.当然,还有一个错误的数字,否则,就是"2A2B"了.

4.您共有8次机会,在8次内猜出"4A0B"的答案,则本局智力挑战成功,将获得10分的奖励;否则,就挑战失败,并将会被扣掉10分.

5.本游戏可以锻炼您的逻辑推理能力,请马上开始挑战吧!

祝您好运!
    '''
    title_about = '关于'
    about = '作者: KomorebiSaw'


class Ui_MainWindow(object):
    def __init__(self):
        # 总共猜对的次数
        self.correct = 0
        # 总共猜错的次数
        self.wrong = 0
        # 单局最多输入次数
        self.max_retry = 8
        self.start = False
        self.debug = False
        self.msg = Message()

        self.count = 0
        self.number = ''

    def set_score(self):
        correct = self.correct
        wrong = self.wrong
        self.guess_correct.setText(str(correct))
        self.guess_wrong.setText(str(wrong))
        score = (correct - wrong) * 10
        self.score.setText(str(score))

    def reset(self):
        # 一局里的计数
        self.count = 1
        # 正确数字
        self.number = self.generate_num()
        # print(self.number)

    @staticmethod
    def generate_num():
        digits = string.digits
        s = ''
        for i in range(4):
            a = random.choice(digits)
            s += a
            digits = digits.replace(a, '')  # not repeat
        return s

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setWindowIcon(QtGui.QIcon('Only.ico'))

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(330, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 11, 31, 16))
        self.label_2.setObjectName("label_2")
        self.user_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(50, 10, 211, 20))
        self.user_input.setMaxLength(4)
        self.user_input.setObjectName("user_input")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(6, 40, 321, 120))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(180, 21, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 56, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(180, 90, 31, 16))
        self.label_5.setObjectName("label_5")
        self.history = QtWidgets.QTextEdit(self.groupBox)
        self.history.setGeometry(QtCore.QRect(10, 20, 142, 90))
        font = QtGui.QFont()
        font.setFamily("simSun")
        font.setPointSize(10)
        self.history.setFont(font)
        self.history.setReadOnly(True)
        self.history.setObjectName("textEdit")
        self.guess_correct = QtWidgets.QLineEdit(self.groupBox)
        self.guess_correct.setGeometry(QtCore.QRect(210, 20, 100, 20))
        self.guess_correct.setReadOnly(True)
        self.guess_correct.setObjectName("lineEdit")
        self.guess_correct.setAlignment(QtCore.Qt.AlignRight)
        self.guess_wrong = QtWidgets.QLineEdit(self.groupBox)
        self.guess_wrong.setGeometry(QtCore.QRect(210, 56, 100, 20))
        self.guess_wrong.setReadOnly(True)
        self.guess_wrong.setObjectName("lineEdit_2")
        self.guess_wrong.setAlignment(QtCore.Qt.AlignRight)
        self.score = QtWidgets.QLineEdit(self.groupBox)
        self.score.setGeometry(QtCore.QRect(210, 90, 100, 20))
        self.score.setReadOnly(True)
        self.score.setObjectName("lineEdit_3")
        self.score.setAlignment(QtCore.Qt.AlignRight)
        self.new_game = QtWidgets.QPushButton(self.centralwidget)
        self.new_game.setGeometry(QtCore.QRect(65, 210, 75, 23))
        self.new_game.setAutoDefault(False)
        self.new_game.setObjectName("new_game")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(185, 210, 75, 23))
        self.exit.setAutoDefault(False)
        self.exit.setDefault(False)
        self.exit.setFlat(False)
        self.exit.setObjectName("exit")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(270, 9, 51, 23))
        self.submit_button.setObjectName("submit_button")
        self.output_info = QtWidgets.QTextEdit(self.centralwidget)
        self.output_info.setGeometry(QtCore.QRect(6, 160, 321, 45))
        self.output_info.setReadOnly(True)
        self.output_info.setObjectName("textEdit_2")
        self.output_info.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setTearOffEnabled(False)
        self.menu.setToolTipsVisible(False)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Game = QtWidgets.QAction(MainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menu.addAction(self.actionNew_Game)
        self.menu.addAction(self.actionExit_2)
        self.menu_2.addAction(self.actionHelp)
        self.menu_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.bind()
        self.set_score()

    def bind(self):
        MainWindow = self.MainWindow

        self.retranslateUi(MainWindow)
        # 退出
        self.exit.clicked.connect(MainWindow.close)
        self.actionExit_2.triggered.connect(MainWindow.close)
        # 提交
        self.submit_button.clicked.connect(self.submit)
        # 按下回车提交
        self.user_input.returnPressed.connect(self.submit)
        # 限制用户输入
        self.user_input.setValidator(QIntValidator())
        self.user_input.setMaxLength(4)
        # 开始游戏
        self.new_game.clicked.connect(self.start_game)
        self.actionNew_Game.triggered.connect(self.start_game)
        # 游戏帮助
        self.actionHelp.triggered.connect(self.show_help)
        # 关于
        self.actionAbout.triggered.connect(self.show_about)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def start_game(self):
        self.reset()
        self.start = True
        self.user_input.setText('')
        self.history.setPlainText('')
        self.output_info.setPlainText(self.msg.start)
        self.output_info.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "逻辑猜数"))
        self.label_2.setText(_translate("MainWindow", "输入"))
        self.groupBox.setTitle(_translate("MainWindow", "历史记录"))
        self.label_3.setText(_translate("MainWindow", "猜对"))
        self.label_4.setText(_translate("MainWindow", "猜错"))
        self.label_5.setText(_translate("MainWindow", "得分"))
        self.new_game.setText(_translate("MainWindow", "新游戏"))
        self.exit.setText(_translate("MainWindow", "退出"))
        self.submit_button.setText(_translate("MainWindow", "提交"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.actionNew_Game.setText(_translate("MainWindow", "新游戏"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "游戏帮助"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionExit_2.setText(_translate("MainWindow", "退出"))

    def show_help(self):
        msg = self.msg.help
        title = self.msg.title_help
        QMessageBox = QtWidgets.QMessageBox
        QMessageBox.information(self.MainWindow, title, msg, QMessageBox.Ok)

    def show_about(self):
        msg = self.msg.about
        title = self.msg.title_about
        QMessageBox = QtWidgets.QMessageBox
        QMessageBox.information(self.MainWindow, title, msg, QMessageBox.Ok)

    def submit(self):
        if self.start is False:
            return

        text = self.user_input.text()
        if len(text) < 4 or len(set(list(text))) < 4:
            self.alert()
            return

        self.user_input.setText('')

        result, end = self.cmp_num(self.number, text)
        self.update_history(text, result)
        self.count += 1

        if end is True:
            self.success()
            return

        if self.count > self.max_retry:
            self.fail()

    def update_history(self, text, result):
        h = '[{}]  {}=>{}\n'.format(self.count, text, result)
        old = self.history.toPlainText()
        new = h + old
        self.history.setPlainText(new)

    def alert(self):
        msg = self.msg.alert
        QMessageBox = QtWidgets.QMessageBox
        QMessageBox.critical(self.MainWindow, '提示', msg, QMessageBox.Ok)

    def success(self):
        msg = self.msg.success
        self.output_info.setPlainText(msg)
        self.output_info.setAlignment(QtCore.Qt.AlignCenter)
        self.start = False
        self.correct += 1
        self.finish()

    def fail(self):
        msg1 = self.msg.fail1
        msg2 = self.msg.fail2.format(self.number)
        self.output_info.setPlainText('')
        self.output_info.setAlignment(QtCore.Qt.AlignCenter)
        self.output_info.insertPlainText(msg1)
        self.output_info.insertPlainText(msg2)
        self.start = False
        self.wrong += 1
        self.finish()

    def finish(self):
        self.set_score()

    def cmp_num(self, number, s):
        n = number
        a = 0
        b = 0
        if n == s:
            return '4A0B', True

        for i in range(4):
            if n[i] == s[i]:
                a += 1
                continue
            if s[i] in n:
                b += 1
        r = '{}A{}B'.format(a, b)
        return r, False
