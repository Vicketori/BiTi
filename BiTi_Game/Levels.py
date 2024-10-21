from PyQt6.QtCore import QTimer, QPropertyAnimation, QPoint, Qt

class Timer_(QTimer):
    def __init__(self, ti, f, type):
        super(Timer_, self).__init__()
        self.label = f
        self.setTimerType(Qt.TimerType.PreciseTimer)
        self.setSingleShot(True)
        if type == 'up':
            self.timeout.connect(self.animate_up)
        if type == 'down':
            self.timeout.connect(self.animate_down)
        if type == 'left':
            self.timeout.connect(self.animate_left)
        if type == 'right':
            self.timeout.connect(self.animate_right)
        self.start(ti)

    def animate_up(self):
        self.label.setGeometry(300, 0, 100, 100)
        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(500)
        self.animation.setEndValue(QPoint(300, 300))
        self.animation.finished.connect(self.off)
        self.animation.start()

    def animate_down(self):
        self.label.setGeometry(300, 600, 100, 100)
        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(500)
        self.animation.setEndValue(QPoint(300, 300))
        self.animation.finished.connect(self.off)
        self.animation.start()

    def animate_left(self):
        self.label.setGeometry(0, 300, 100, 100)
        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(500)
        self.animation.setEndValue(QPoint(300, 300))
        self.animation.finished.connect(self.off)
        self.animation.start()

    def animate_right(self):
        self.label.setGeometry(600, 300, 100, 100)
        self.animation = QPropertyAnimation(self.label, b"pos")
        self.animation.setDuration(500)
        self.animation.setEndValue(QPoint(300, 300))
        self.animation.finished.connect(self.off)
        self.animation.start()

    def off(self):
        self.label.setGeometry(0, 0, 0, 0)


class Timer_win(QTimer):
    def __init__(self, t, lvl, w, game):
        super(Timer_win, self).__init__()
        self.setTimerType(Qt.TimerType.PreciseTimer)
        self.setSingleShot(True)
        self.timeout.connect(lambda: self.lvl_win(game))
        self.start(t)
        self.label1 = lvl
        self.label2 = w

    def lvl_win(self, game):
        self.label1.setGeometry(0, 0, 0, 0)
        self.label2.setGeometry(0, 0, 1920, 1080)
        if game.miss + game.hit_300 + game.hit_100 >= len(game.timer_ti):
            if game.combo > 0:
                game.score *= game.combo
            file = open("text/record" + str(game.selected_level + 1) + ".txt", 'r')
            lines = file.readlines()
            game.record_combo, game.record_score, game.record_accuracy = [line.strip() for line in lines]
            file.close()
            if int(game.record_score) < game.score:
                file = open("text/record" + str(game.selected_level + 1) + ".txt", 'w')
                file.write(str(game.combo) + '\n' + str(game.score) + '\n' + str(round(game.accuracy)))
                file.close()
                game.record_combo_sm.setText(str(game.combo))
                game.record_score_sm.setText(str(game.score))
                game.record_accuracy_sm.setText(str(round(game.accuracy)))

        else:
            self.label2.setGeometry(0, 0, 0, 0)
            game.lose.setGeometry(0, 0, 1920, 1080)
            game.lose_lbl_lose.setText("Вы проиграли \n Не обманете")

        game.combo_tx_win.setText(str(game.combo))
        game.score_tx_win.setText(str(game.score))
        game.accuracy_tx_win.setText(str(round(game.accuracy)))


def lvl_on(self):
    self.lc_1.setGeometry(0, 0, 0, 0)
    self.lc_2.setGeometry(0, 0, 0, 0)
    self.lc_3.setGeometry(0, 0, 0, 0)
    self.lc_4.setGeometry(0, 0, 0, 0)
    self.lc_5.setGeometry(0, 0, 0, 0)

    self.lc_6.setGeometry(0, 0, 0, 0)
    self.lc_7.setGeometry(0, 0, 0, 0)
    self.lc_8.setGeometry(0, 0, 0, 0)
    self.lc_9.setGeometry(0, 0, 0, 0)
    self.lc_0.setGeometry(0, 0, 0, 0)

    self.score = 0
    self.accuracy = 100
    self.combo = 0
    self.miss = 0
    self.hit_300 = 0
    self.hit_100 = 0
    self.check = False
    self.lose_check = True
    self.check_combo = 0
    self.combo_tx.setText(str(self.combo))
    self.score_tx.setText(str(self.score))
    self.accuracy_tx.setText(str(self.accuracy))


def Hit(hit, key_timers):
    for _ in range(len(key_timers)):
        hit.append(False)


def timers_ti_type(key_timers_W, key_timers_A, key_timers_S, key_timers_D):
    timer_ti = key_timers_W + key_timers_A + key_timers_S + key_timers_D
    timer_ti.sort()
    timer_type = []
    for i in range(0, len(timer_ti)):
        if timer_ti[i] in key_timers_W:
            timer_type.append('up')
        elif timer_ti[i] in key_timers_A:
            timer_type.append('left')
        elif timer_ti[i] in key_timers_S:
            timer_type.append('down')
        else:
            timer_type.append('right')
        timer_ti[i] = int(timer_ti[i] * 1000 - 400)
    return(timer_ti, timer_type)


def s_lvl_1(self):
    self.lvl_1.setGeometry(610, 190, 700, 700)
    lvl_on(self)
    self.mus_lvl_1.play()

    self.key_timers_W = [0.5, 8.3, 17.8, 21.9, 22.15, 23.1, 25.4, 31.3]
    self.hit_W = []
    Hit(self.hit_W, self.key_timers_W)
    self.key_timers_A = [5.8, 15.7, 16.3, 18.6, 19.2, 20.8, 22.3, 24.7, 27.2, 30.3, 31.0]
    self.hit_A = []
    Hit(self.hit_A, self.key_timers_A)
    self.key_timers_S = [13.4, 13.9, 21.1, 24.4, 25.1, 26.9, 27.9, 28.2, 30.0, 30.6]
    self.hit_S = []
    Hit(self.hit_S, self.key_timers_S)
    self.key_timers_D = [3.1, 11.3, 20.5, 21.4, 22.8, 25.7, 27.5, 31.4]
    self.hit_D = []
    Hit(self.hit_D, self.key_timers_D)

    self.timer_ti, self.timer_type = timers_ti_type(self.key_timers_W, self.key_timers_A, self.key_timers_S, self.key_timers_D)
    self.timers = []

    for i in range(0, len(self.timer_ti)):
        timer_f = [self.lc_1, self.lc_2, self.lc_3, self.lc_4, self.lc_5]
        timer = Timer_(self.timer_ti[i], timer_f[i % 5], self.timer_type[i])
        self.timers.append(timer)

    self.time_to_win = Timer_win(33000, self.lvl_1, self.win, self)


def s_lvl_2(self):
    self.lvl_2.setGeometry(610, 190, 700, 700)
    lvl_on(self)
    self.mus_lvl_2.play()

    self.key_timers_W = [3.0, 6.7, 12.5, 13.5, 16.9, 18.6, 20.6, 22.2, 23.5, 23.8, 26.2, 27.8, 28.6, 29.1, 32.3]
    self.hit_W = []
    Hit(self.hit_W, self.key_timers_W)
    self.key_timers_A = [1.2, 4.6, 8.8, 14.2, 15.3, 18.1, 18.9, 19.7, 22.7, 24.3, 25.4, 27.5, 28.3, 29.4, 31.0]
    self.hit_A = []
    Hit(self.hit_A, self.key_timers_A)
    self.key_timers_S = [6.4, 7.9, 11.1, 13.8, 15.8, 17.3, 20.3, 21.1, 23.0, 24.6, 25.9, 27.0, 29.9, 30.2, 31.5]
    self.hit_S = []
    Hit(self.hit_S, self.key_timers_S)
    self.key_timers_D = [2.5, 9.6, 14.5, 15, 16.1, 16.6, 17.7, 19.4, 21.4, 21.9, 25.1, 26.7, 30.7, 31.8]
    self.hit_D = []
    Hit(self.hit_D, self.key_timers_D)

    self.timer_ti, self.timer_type = timers_ti_type(self.key_timers_W, self.key_timers_A, self.key_timers_S,
                                                    self.key_timers_D)
    self.timers = []

    for i in range(0, len(self.timer_ti)):
        timer_f = [self.lc_6, self.lc_7, self.lc_8, self.lc_9, self.lc_0]
        timer = Timer_(self.timer_ti[i], timer_f[i % 5], self.timer_type[i])
        self.timers.append(timer)

    self.time_to_win = Timer_win(39000, self.lvl_2, self.win, self)


def s_lvl_3(self):
    lvl_on(self)
    self.lvl_3.setGeometry(0, 0, 1920, 1080)
    self.bg_will_be_later.setGeometry(0, 0, 1920, 1080)
    self.will_be_later.setGeometry(755, 450, 700, 100)
