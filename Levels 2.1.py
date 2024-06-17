from PyQt6.QtCore import QTimer, QPropertyAnimation, QPoint, Qt
from Frames import win_f


class Timer_up(QTimer):
    def __init__(self, t, f):
        super(Timer_up, self).__init__()
        self.label = f
        self.setTimerType(Qt.TimerType.PreciseTimer)
        self.setSingleShot(True)
        self.timeout.connect(self.animate_f)
        self.start(t)

    def animate_f(self):
        self.label.setGeometry(300, 0, 100, 100)
        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(500)
        self.animation.setEndValue(QPoint(300, 300))
        self.animation.finished.connect(self.off)
        self.animation.start()

    def off(self):
        self.label.setGeometry(0, 0, 0, 0)


class Timer_down(QTimer):
    def __init__(self, t, f):
        super(Timer_down, self).__init__()
        self.label = f
        self.setTimerType(Qt.TimerType.PreciseTimer)
        self.setSingleShot(True)
        self.timeout.connect(self.animate_f)
        self.start(t)

    def animate_f(self):
        self.label.setGeometry(300, 600, 100, 100)
        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(500)
        self.animation.setEndValue(QPoint(300, 300))
        self.animation.finished.connect(self.off)
        self.animation.start()

    def off(self):
        self.label.setGeometry(0, 0, 0, 0)


class Timer_left(QTimer):
    def __init__(self, t, f):
        super(Timer_left, self).__init__()
        self.label = f
        self.setTimerType(Qt.TimerType.PreciseTimer)
        self.setSingleShot(True)
        self.timeout.connect(self.animate_f)
        self.start(t)

    def animate_f(self):
        self.label.setGeometry(0, 300, 100, 100)
        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(500)
        self.animation.setEndValue(QPoint(300, 300))
        self.animation.finished.connect(self.off)
        self.animation.start()

    def off(self):
        self.label.setGeometry(0, 0, 0, 0)


class Timer_right(QTimer):
    def __init__(self, t, f):
        super(Timer_right, self).__init__()
        self.label = f
        self.setTimerType(Qt.TimerType.PreciseTimer)
        self.setSingleShot(True)
        self.timeout.connect(self.animate_f)
        self.start(t)

    def animate_f(self):
        self.label.setGeometry(600, 300, 100, 100)
        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(500)
        self.animation.setEndValue(QPoint(300, 300))
        self.animation.finished.connect(self.off)
        self.animation.start()

    def off(self):
        self.label.setGeometry(0, 0, 0, 0)

class Timer_win(QTimer):
    def __init__(self, t, l, w):
        super(Timer_win, self).__init__()
        self.setTimerType(Qt.TimerType.PreciseTimer)
        self.setSingleShot(True)
        self.timeout.connect(self.lvl_win)
        self.start(t)
        self.label1 = l
        self.label2 = w

    def lvl_win(self):
        self.label1.setGeometry(0, 0, 0, 0)
        self.label2.setGeometry(0, 0, 1920, 1080)


def s_lvl_1(self):
    self.lvl_1.setGeometry(610, 190, 700, 700)
    lvl_off(self)
    self.mus_lvl_1.play()

    #слайдеры
    self.ss_1 = Timer_up(100, self.ls_start_1)
    self.se_1 = Timer_up(2700, self.ls_end_1)
    self.ss_2 = Timer_right(2700, self.ls_start_2)
    self.se_2 = Timer_right(5400, self.ls_end_2)
    self.ss_3 = Timer_left(5400, self.ls_start_3)
    self.se_3 = Timer_left(7900, self.ls_end_3)
    self.ss_4 = Timer_up(7900, self.ls_start_1)
    self.se_4 = Timer_up(10900, self.ls_end_1)
    #ноты
    self.sc_1 = Timer_right(10900, self.lc_1)
    self.sc_2 = Timer_down(13000, self.lc_2)
    self.sc_3 = Timer_down(13500, self.lc_3)
    self.sc_4 = Timer_left(15300, self.lc_4)
    self.sc_5 = Timer_left(15900, self.lc_5)
    self.sc_6 = Timer_up(17400, self.lc_1)
    self.sc_7 = Timer_left(18300, self.lc_2)
    self.sc_8 = Timer_left(18800, self.lc_3)
    self.sc_9 = Timer_right(20100, self.lc_4)
    self.sc_10 = Timer_left(20400, self.lc_5)
    self.sc_11 = Timer_down(20700, self.lc_1)
    self.sc_12 = Timer_right(21000, self.lc_2)
    self.sc_13 = Timer_up(21200, self.lc_3)
    self.sc_14 = Timer_up(21800, self.lc_4)
    self.sc_15 = Timer_up(21100, self.lc_5)
    # self.sc_16 = Timer_up(21200, self.lc_6)
    # self.sc_17 = Timer_up(21200, self.lc_7)
    # self.sc_18 = Timer_up(21200, self.lc_8)
    # self.sc_19 = Timer_up(21200, self.lc_9)
    # self.sc_20 = Timer_up(21200, self.lc_10)

    self.time_to_win = Timer_win(33000, self.lvl, self.win)


def s_lvl_2(self):
    self.lvl_2.setGeometry(610, 190, 700, 700)
    lvl_off(self)
    self.mus_lvl_2.play()

    self.time_to_win = Timer_win(3000, self.lvl, self.win)


def s_lvl_3(self):
    lvl_off(self)
    self.lvl_3.setGeometry(0, 0, 1920, 1080)
    self.bg_will_be_later.setGeometry(0, 0, 1920, 1080)
    self.will_be_later.setGeometry(755, 450, 700, 100)


def lvl_off(self):
    self.ls_start_1.setGeometry(0, 0, 0, 0)
    self.ls_end_1.setGeometry(0, 0, 0, 0)
    self.ls_start_2.setGeometry(0, 0, 0, 0)
    self.ls_end_2.setGeometry(0, 0, 0, 0)
    self.ls_start_3.setGeometry(0, 0, 0, 0)
    self.ls_end_3.setGeometry(0, 0, 0, 0)

    self.lc_1.setGeometry(0, 0, 0, 0)
    self.lc_2.setGeometry(0, 0, 0, 0)
    self.lc_3.setGeometry(0, 0, 0, 0)
    self.lc_4.setGeometry(0, 0, 0, 0)
    self.lc_5.setGeometry(0, 0, 0, 0)

    self.lr_1.setGeometry(0, 0, 0, 0)