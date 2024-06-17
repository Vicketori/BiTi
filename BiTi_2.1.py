import sys
import ctypes

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QIcon, QPixmap, QFontDatabase
from PyQt6.QtCore import QSize, QUrl
from Frames import mm_f, sm_f, lvl_f, st_f, sk_f, win_f, lose_f
from Levels import s_lvl_1, s_lvl_2, s_lvl_3
from PyQt6.QtMultimedia import QSoundEffect


class GameObj(object):
    def setupUi(self, Game):
        self.centralwidget = QWidget(parent=Game)
        Game.setCentralWidget(self.centralwidget)

        # музыка в главном меню
        self.mus_mm = QSoundEffect()
        self.mus_mm.setSource(QUrl.fromLocalFile("music/mm.wav"))
        self.mus_mm.setLoopCount(-2)

        self.mus_lvl_1 = QSoundEffect()
        self.mus_lvl_1.setSource(QUrl.fromLocalFile("music/simphony_1.wav"))

        self.mus_lvl_2 = QSoundEffect()
        self.mus_lvl_2.setSource(QUrl.fromLocalFile("music/Nadezhda.wav"))

        self.eff_clap = QSoundEffect()
        self.eff_clap.setSource(QUrl.fromLocalFile("music/clap.wav"))

        self.eff_loss = QSoundEffect()
        self.eff_loss.setSource(QUrl.fromLocalFile("music/loss_of_combo.wav"))

        volume = open("text/volume_m.txt")
        v_m = volume.read()
        volume.close()

        volume = open("text/volume_e.txt")
        v_e = volume.read()
        volume.close()

        self.mus_mm.setVolume(float(v_m)/100)
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

        if self.selected_level == 0:
            self.mus_mm.stop()
            s_lvl_1(self)
        if self.selected_level == 1:
            self.mus_mm.stop()
            s_lvl_2(self)
        if self.selected_level == 2:
            s_lvl_3(self)

        skin_txt = open("text/skins.txt")
        skin = skin_txt.read()
        skin_txt.close()
        self.bg_lvl.setPixmap(QPixmap("design/skins/" + skin + "/bg.png"))

        self.music_name.setText(self.list_song[self.selected_level])
        self.singer_name.setText(self.list_singer[self.selected_level])

    def arrow_plus(self):
        if self.selected_level == 0:
            self.selected_level = self.max_level
        else:
            self.selected_level -= 1
        self.song.setText(self.list_song[self.selected_level])
        self.singer.setText(self.list_singer[self.selected_level])

    def arrow_minus(self):
        if self.selected_level == self.max_level:
            self.selected_level = 0

        else:
            self.selected_level +=1
        self.song.setText(self.list_song[self.selected_level])
        self.singer.setText(self.list_singer[self.selected_level])

    def lvl_sm(self):
        self.lvl.setGeometry(0, 0, 0, 0)
        self.sm.setGeometry(0, 0, 1920, 1080)
        self.lvl_1.setGeometry(0, 0, 0, 0)
        self.lvl_2.setGeometry(0, 0, 0, 0)
        self.lvl_3.setGeometry(0, 0, 0, 0)
        if self.time_to_win.isActive():
            self.time_to_win.stop()
        self.mus_lvl_1.stop()
        self.mus_lvl_2.stop()
        self.mus_mm.play()

    def w_again(self):
        self.win.setGeometry(0, 0, 0, 0)
        self.lvl.setGeometry(0, 0, 1920, 1080)

        if self.selected_level == 0:
            s_lvl_1(self)
        if self.selected_level == 1:
            s_lvl_2(self)
        if self.selected_level == 2:
            s_lvl_3(self)

    def w_mm(self):
        self.win.setGeometry(0, 0, 0, 0)
        self.mm.setGeometry(0, 0, 1920, 1080)
        self.mus_mm.play()

    def w_sm(self):
        self.win.setGeometry(0, 0, 0, 0)
        self.sm.setGeometry(0, 0, 1920, 1080)
        self.mus_mm.play()

    def mus_off(self):
        if self.mus_lvl_1.isPlaying():
            self.mus_lvl_1.stop()
        if self.mus_lvl_2.isPlaying():
            self.mus_lvl_2.stop()

    def l_again(self):
        self.lose.setGeometry(0, 0, 0, 0)
        self.lvl.setGeometry(0, 0, 1920, 1080)
        mus_off(self)

        if self.selected_level == 0:
            s_lvl_1(self)
        if self.selected_level == 1:
            s_lvl_2(self)
        if self.selected_level == 2:
            s_lvl_3(self)

    def l_mm(self):
        self.lose.setGeometry(0, 0, 0, 0)
        self.mm.setGeometry(0, 0, 1920, 1080)
        self.mus_mm.play()
        self.mus_off(self)

    def l_sm(self):
        self.lose.setGeometry(0, 0, 0, 0)
        self.sm.setGeometry(0, 0, 1920, 1080)
        self.mus_mm.play()
        self.mus_off(self)

app = QApplication(sys.argv)
window = QMainWindow()
ui = GameObj()
ui.setupUi(window)

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
