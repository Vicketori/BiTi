import sys
import ctypes
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QIcon, QPixmap, QFontDatabase
from PyQt6.QtCore import QSize, QUrl, Qt
from Frames import mm_f, sm_f, lvl_f, st_f, sk_f, win_f, lose_f
from Levels import s_lvl_1, s_lvl_2, s_lvl_3
from PyQt6.QtMultimedia import QSoundEffect


class Music(QSoundEffect):
    def __init__(self, a):
        super(Music, self).__init__()
        self.setSource(QUrl.fromLocalFile(a))


class Game(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.lvl_1_ON = False
        self.lvl_2_ON = False

        # музыка в главном меню
        self.mus_mm = Music("music/mm.wav")
        self.mus_mm.setLoopCount(-2)

        self.mus_lvl_1 = Music("music/simphony_1.wav")
        self.mus_lvl_2 = Music("music/Nadezhda.wav")
        self.eff_clap = Music("music/clap.wav")
        self.eff_loss = Music("music/loss_of_combo.wav")

        volume = open("text/volume_m.txt")
        v_m = volume.read()
        volume.close()

        volume = open("text/volume_e.txt")
        v_e = volume.read()
        volume.close()

        self.mus_mm.setVolume(float(v_m) / 100)
        self.mus_lvl_1.setVolume(float(v_m) / 100)
        self.mus_lvl_2.setVolume(float(v_m) / 100)
        self.eff_clap.setVolume(float(v_e) / 100)
        self.eff_loss.setVolume(float(v_e) / 100)

        self.mus_mm.play()

        mm_f(self)
        self.start.clicked.connect(self.mm_sm)
        self.settings.clicked.connect(self.mm_st)
        self.skins.clicked.connect(self.mm_sk)
        self.quit.clicked.connect(app.quit)

        sk_f(self)
        self.sk_panel1.clicked.connect(self.sk_1)
        self.sk_panel2.clicked.connect(self.sk_2)
        self.sk_panel3.clicked.connect(self.sk_3)
        self.sk_goto_mm.clicked.connect(self.sk_mm)

        st_f(self)
        self.st_goto_mm.clicked.connect(self.st_mm)

        sm_f(self)
        self.sm_goto_mm.clicked.connect(self.sm_mm)
        self.central_field_sm.clicked.connect(self.sm_lvl)
        self.arrow_up.clicked.connect(self.arrow_plus)
        self.arrow_down.clicked.connect(self.arrow_minus)

        lvl_f(self)
        self.goto_sm.clicked.connect(self.lvl_sm)

        win_f(self)
        self.again_w.clicked.connect(self.w_again)
        self.w_goto_mm.clicked.connect(self.w_mm)
        self.w_goto_sm.clicked.connect(self.w_sm)

        lose_f(self)
        self.again_l.clicked.connect(self.l_again)
        self.l_goto_mm.clicked.connect(self.l_mm)
        self.l_goto_sm.clicked.connect(self.l_sm)

    def mm_sm(self):
        self.mm.setGeometry(0, 0, 0, 0)
        self.sm.setGeometry(0, 0, 1920, 1080)

    def mm_st(self):
        self.mm.setGeometry(0, 0, 0, 0)
        self.st.setGeometry(0, 0, 1920, 1080)

    def mm_sk(self):
        self.mm.setGeometry(0, 0, 0, 0)
        self.sk.setGeometry(0, 0, 1920, 1080)

    def sk_1(self):
        skin_t = open("text/skins.txt", 'w')
        skin_t.write("1")
        skin_t.close()
        self.sk_lbl_bg.setPixmap(QPixmap("design/skins/1/bg_mini.png"))

    def sk_2(self):
        skin_t = open("text/skins.txt", 'w')
        skin_t.write("2")
        skin_t.close()
        self.sk_lbl_bg.setPixmap(QPixmap("design/skins/2/bg_mini.png"))

    def sk_3(self):
        skin_t = open("text/skins.txt", 'w')
        skin_t.write("3")
        skin_t.close()
        self.sk_lbl_bg.setPixmap(QPixmap("design/skins/3/bg_mini.png"))

    def sk_mm(self):
        self.sk.setGeometry(0, 0, 0, 0)
        self.mm.setGeometry(0, 0, 1920, 1080)

    def st_mm(self):
        self.st.setGeometry(0, 0, 0, 0)
        self.mm.setGeometry(0, 0, 1920, 1080)

    def sm_mm(self):
        self.sm.setGeometry(0, 0, 0, 0)
        self.mm.setGeometry(0, 0, 1920, 1080)

    def sm_lvl(self):
        self.sm.setGeometry(0, 0, 0, 0)
        self.lvl.setGeometry(0, 0, 1920, 1080)
        self.a = time.time()

        if self.selected_level == 0:
            if self.mus_mm.isPlaying():
                self.mus_mm.stop()
            self.lvl_1_ON = True
            s_lvl_1(self)
        if self.selected_level == 1:
            if self.mus_mm.isPlaying():
                self.mus_mm.stop()
            self.lvl_2_ON = True
            s_lvl_2(self)
        if self.selected_level == 2:
            s_lvl_3(self)

        skin_txt = open("text/skins.txt")
        skin = skin_txt.read()
        skin_txt.close()
        self.bg_lvl.setPixmap(QPixmap("design/skins/" + skin + "/bg.png"))
        self.lc_1.setPixmap(QPixmap("design/skins/" + skin + "/circle.png"))
        self.lc_2.setPixmap(QPixmap("design/skins/" + skin + "/circle.png"))
        self.lc_3.setPixmap(QPixmap("design/skins/" + skin + "/circle.png"))
        self.lc_4.setPixmap(QPixmap("design/skins/" + skin + "/circle.png"))
        self.lc_5.setPixmap(QPixmap("design/skins/" + skin + "/circle.png"))

        self.score = 0
        self.accuracy = 100
        self.combo = 0
        self.miss = 0
        self.hit_300 = 0
        self.hit_100 = 0
        self.check = False
        self.lose_check = True
        self.check_combo = 0

        self.music_name.setText(self.list_song[self.selected_level])
        self.singer_name.setText(self.list_singer[self.selected_level])

    def arrow_plus(self):
        if self.selected_level == 0:
            self.selected_level = self.max_level
        else:
            self.selected_level -= 1
        self.song.setText(self.list_song[self.selected_level])
        self.singer.setText(self.list_singer[self.selected_level])

        file = open("text/record" + str(self.selected_level + 1) + ".txt")
        lines = file.readlines()
        self.record_combo, self.record_score, self.record_accuracy = [line.strip() for line in lines]
        self.record_combo_sm.setText(self.record_combo)
        self.record_score_sm.setText(self.record_score)
        self.record_accuracy_sm.setText(self.record_accuracy)
        file.close()

    def arrow_minus(self):
        if self.selected_level == self.max_level:
            self.selected_level = 0

        else:
            self.selected_level += 1
        self.song.setText(self.list_song[self.selected_level])
        self.singer.setText(self.list_singer[self.selected_level])

        file = open("text/record" + str(self.selected_level + 1) + ".txt")
        lines = file.readlines()
        self.record_combo, self.record_score, self.record_accuracy = [line.strip() for line in lines]
        self.record_combo_sm.setText(self.record_combo)
        self.record_score_sm.setText(self.record_score)
        self.record_accuracy_sm.setText(self.record_accuracy)
        file.close()

    def lvl_sm(self):
        self.lvl.setGeometry(0, 0, 0, 0)
        self.sm.setGeometry(0, 0, 1920, 1080)
        self.lvl_1.setGeometry(0, 0, 0, 0)
        self.lvl_2.setGeometry(0, 0, 0, 0)
        self.lvl_3.setGeometry(0, 0, 0, 0)
        self.lvl_1_ON = False
        self.lvl_2_ON = False
        self.time_to_win.stop()
        if self.mus_lvl_1.isPlaying():
            self.mus_lvl_1.stop()
        if self.mus_lvl_2.isPlaying():
            self.mus_lvl_2.stop()
        self.mus_mm.play()

    def w_again(self):
        self.win.setGeometry(0, 0, 0, 0)
        self.sm_lvl()

        if self.selected_level == 0:
            s_lvl_1(self)
        if self.selected_level == 1:
            s_lvl_2(self)

    def w_mm(self):
        self.win.setGeometry(0, 0, 0, 0)
        self.lvl.setGeometry(0, 0, 0, 0)
        self.mm.setGeometry(0, 0, 1920, 1080)
        self.mus_mm.play()

    def w_sm(self):
        self.win.setGeometry(0, 0, 0, 0)
        self.lvl.setGeometry(0, 0, 0, 0)
        self.sm.setGeometry(0, 0, 1920, 1080)
        self.mus_mm.play()

    def l_again(self):
        self.lose.setGeometry(0, 0, 0, 0)
        self.lose_lbl_lose.setText("Вы проиграли")
        self.sm_lvl()
        self.time_to_win.stop()
        if self.selected_level == 0:
            s_lvl_1(self)
        if self.selected_level == 1:
            s_lvl_2(self)

    def l_mm(self):
        self.lose.setGeometry(0, 0, 0, 0)
        self.lvl.setGeometry(0, 0, 0, 0)
        self.lose_lbl_lose.setText("Вы проиграли")
        self.time_to_win.stop()
        self.mm.setGeometry(0, 0, 1920, 1080)
        self.mus_lvl_off()

    def l_sm(self):
        self.lose.setGeometry(0, 0, 0, 0)
        self.lvl.setGeometry(0, 0, 0, 0)
        self.lose_lbl_lose.setText("Вы проиграли")
        self.time_to_win.stop()
        self.sm.setGeometry(0, 0, 1920, 1080)
        self.mus_lvl_off()

    def mus_lvl_off(self):
        self.mus_mm.play()
        if self.mus_lvl_1.isPlaying():
            self.mus_lvl_1.stop()
        if self.mus_lvl_2.isPlaying():
            self.mus_lvl_2.stop()

    def keyPressEvent(self, event):
        def Key_time(i, t_k, hit):
            t = time.time()
            t_k += 0.15

            if t >= self.a + t_k - 0.07 and t <= self.a + t_k + 0.07 and hit[i] == False:
                self.score += 300
                self.combo += 1
                self.check_combo = self.miss
                self.miss -= 1
                self.hit_300 += 1
                self.eff_clap.play()
                self.check = True
                hit[i] = True
            elif t >= self.a + t_k - 0.15 and t <= self.a + t_k + 0.15 and hit[i] == False:
                self.score += 100
                self.combo += 1
                self.check_combo = self.miss
                self.miss -= 1
                self.hit_100 += 1
                self.eff_clap.play()
                self.check = True
                hit[i] = True
            else:
                self.check = True
            self.combo_tx.setText(str(self.combo))
            self.score_tx.setText(str(self.score))


        def Key_timers(key_timers, hit):
            for i in range(len(key_timers)):
                Key_time(i, key_timers[i], hit)
            if self.check:
                self.miss += 1
            if self.miss != self.check_combo:
                self.eff_loss.play()
                self.combo = 0
                self.combo_tx.setText(str(self.combo))
            self.accuracy = 100 * (300 * self.hit_300 + 100 * self.hit_100)/(300*(self.hit_300 + self.hit_100 + self.miss))
            if self.accuracy < 33:
                self.lose.setGeometry(0, 0, 1920, 1080)
                self.lvl.setGeometry(0, 0, 0, 0)
                self.time_to_win.stop()
                self.lose_check = False

                self.score = 0
                self.accuracy = 100
                self.combo = 0
                self.miss = 0
                self.hit_300 = 0
                self.hit_100 = 0
            self.accuracy_tx.setText(str(round(self.accuracy)))

        def Key_check():
            if self.lose_check:
                if event.key() == Qt.Key.Key_W:
                    Key_timers(self.key_timers_W, self.hit_W)
                if event.key() == Qt.Key.Key_A:
                    Key_timers(self.key_timers_A, self.hit_A)
                if event.key() == Qt.Key.Key_S:
                    Key_timers(self.key_timers_S, self.hit_S)
                if event.key() == Qt.Key.Key_D:
                    Key_timers(self.key_timers_D, self.hit_D)

        if self.lvl_1_ON:
            Key_check()
        if self.lvl_2_ON:
            Key_check()




app = QApplication(sys.argv)
window = Game()

#шрифт без установки
QFontDatabase.addApplicationFont("text/Architun.ttf")

#иконка окна
window.setWindowIcon(QIcon(QPixmap("design/icon.png")))

#иконка на панели задач
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window.setIconSize(QSize(32, 32))
window.setWindowTitle("BiTi")
window.showFullScreen()
app.exec()
