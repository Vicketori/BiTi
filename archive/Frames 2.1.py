from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QSlider
from PyQt6.QtGui import QIcon, QPixmap, QCursor
from PyQt6.QtCore import QSize, QPropertyAnimation, QPoint, Qt

from Fonts import font1, font2, font3, font4

#пока затычка
score_num = 3
combo_num = 7
accuracy_num = 68


class Frame(QFrame):
    def __init__(self, x, y, w, h, parent=None):
        super(Frame, self).__init__(parent)
        self.setGeometry(x, y, w, h)


class PushButton(QPushButton):
    def __init__(self, a, b, x, y, w, h, parent=None):
        super(PushButton, self).__init__(parent)
        self.icon_1 = QIcon()
        self.icon_1.addPixmap(QPixmap(a))
        self.setIconSize(QSize(w, h))
        self.setIcon(self.icon_1)

        self.icon_2 = QIcon()
        self.icon_2.addPixmap(QPixmap(b))
        self.setIconSize(QSize(w, h))

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setStyleSheet('border:none')
        self.setGeometry(x, y, w, h)

    def enterEvent(self, event):
        self.setIcon(self.icon_2)

    def leaveEvent(self, event):
        self.setIcon(self.icon_1)


class LabelPng(QLabel):
    def __init__(self, a, x, y, w, h, parent=None):
        super(LabelPng, self).__init__(parent)
        self.setGeometry(x, y, w, h)
        self.setPixmap(QPixmap(a))


class LabelText(QLabel):
    def __init__(self, f, x, y, w, h, r, g, b, t, parent=None):
        super(LabelText, self).__init__(parent)
        self.setGeometry(x, y, w, h)
        self.setFont(f)
        self.setStyleSheet('color: rgb('+str(r)+','+str(g)+','+str(b)+')')
        self.setText(str(t))


def mm_f(self):
    self.mm = Frame(0, 0, 1920, 1080, self.centralwidget)
    # анимация фона
    self.bg_mm = LabelPng("design/mm/bg_1.png", 0, -1750, 1920, 2830, self.mm)
    self.anim = QPropertyAnimation(self.bg_mm, b"pos")
    self.anim.setEndValue(QPoint(0, 0))
    self.anim.setDuration(5500)
    self.anim.setLoopCount(-2)
    self.anim.start()
    self.bg_mmef = LabelPng("design/mm/bg_2.png", 0, 0, 1920, 1080, self.mm)
    self.BiTi = LabelPng("design/mm/BiTi.png", 607, 124, 734, 422, self.mm)

    self.start = PushButton("design/mm/start.png", "design/mm/start_s.png", 580, 618, 760, 121, self.mm)
    self.skins = PushButton("design/mm/skins.png", "design/mm/skins_s.png", 580, 790, 360, 121, self.mm)
    self.quit = PushButton("design/mm/quit.png", "design/mm/quit_s.png", 980, 790, 360, 121, self.mm)
    self.settings = PushButton("design/mm/settings.png", "design/mm/settings_s.png", 1739, 909, 121, 121, self.mm)


def sk_f(self):
    self.sk = Frame(0, 0, 0, 0, self.centralwidget)
    self.bg_sk = LabelPng("design/sk/bg.png", 0, 0, 1920, 1080, self.sk)
    self.sk_goto_mm = PushButton("design/sk/goto_mm.png", "design/sk/goto_mm_s.png", 41, 52, 760, 121, self.sk)
    self.sk_lbl = LabelPng("design/sk/skins.png", 1100, 5, 715, 275, self.sk)
    self.sk_panel1 = PushButton("design/sk/panel1.png", "design/sk/panel1_s.png", 435, 260, 150, 150, self.sk)
    self.sk_panel2 = PushButton("design/sk/panel2.png", "design/sk/panel2_s.png", 885, 260, 150, 150, self.sk)
    self.sk_panel3 = PushButton("design/sk/panel3.png", "design/sk/panel3_s.png", 1335, 260, 150, 150, self.sk)
    skin_t = open("text/skins.txt")
    skin = skin_t.read()
    skin_t.close()
    self.sk_lbl_bg = LabelPng("design/skins/"+skin+"/bg_mini.png", 160, 570, 1600, 400, self.sk)


def st_f(self):
    self.st = Frame(0, 0, 0, 0, self.centralwidget)
    self.bg_st = LabelPng("design/st/bg.png", 0, 0, 1920, 1080, self.st)
    self.st_lbl = LabelPng("design/st/settings.png", 460, 344, 1000, 200, self.st)
    self.st_music = LabelPng("design/st/slider.png", 210, 615, 1500, 50, self.st)
    self.st_effects = LabelPng("design/st/slider.png", 210, 800, 1500, 50, self.st)
    self.st_goto_mm = PushButton("design/st/goto_mm.png", "design/st/goto_mm_s.png", 41, 52, 760, 121, self.st)

    with open("text/volume_m.txt", "r") as f:
        v_m = f.read()

    self.slider_m = QSlider(Qt.Orientation.Horizontal, self.st)
    self.slider_m.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    self.slider_m.setGeometry(220, 625, 1480, 30)
    self.slider_m.setRange(0, 100)
    self.slider_m.setValue(int(v_m))
    self.slider_m.valueChanged.connect(lambda value: updateMusicVolume(self, value))
    self.slider_m.setStyleSheet("QSlider::groove:horizontal {background: rgb(79, 246, 247); border-radius: 15px} QSlider::handle:horizontal {background: rgb(0, 112, 153); width: 30px}")
    self.slider_m.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.slider_m.setPageStep(5)

    with open("text/volume_e.txt", "r") as f:
        v_e = f.read()

    self.slider_e = QSlider(Qt.Orientation.Horizontal, self.st)
    self.slider_e.setFocusPolicy(Qt.FocusPolicy.NoFocus)
    self.slider_e.setGeometry(220, 810, 1480, 30)
    self.slider_e.setRange(0, 100)
    self.slider_e.setValue(int(v_e))
    self.slider_e.valueChanged.connect(lambda value: updateEffectsVolume(self, value))
    self.slider_e.setStyleSheet("QSlider::groove:horizontal {background: rgb(79, 246, 247); border-radius: 15px;} QSlider::handle:horizontal {background: rgb(0, 112, 153); width: 30px}")
    self.slider_e.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.slider_m.setPageStep(5)

    self.m_lbl = LabelText(font2, 210, 545, 220, 70, 21, 59, 71, "Музыка", self.st)
    self.ef_lbl = LabelText(font2, 210, 730, 220, 70, 21, 59, 71, "Эффекты", self.st)
    self.st_m_num = LabelText(font2, 1620, 660, 100, 70, 21, 59, 71, v_m, self.st)
    self.st_e_num = LabelText(font2, 1620, 845, 100, 70, 21, 59, 71, v_e, self.st)


def updateMusicVolume(self, value):
    self.st_m_num.setText(str(value))
    with open("text/volume_m.txt", "w") as f:
        self.mus_mm.setVolume(float(value) / 100)
        self.mus_lvl_1.setVolume(float(value) / 100)
        self.mus_lvl_2.setVolume(float(value) / 100)
        f.write(str(value))


def updateEffectsVolume(self, value):
    self.st_e_num.setText(str(value))
    with open("text/volume_e.txt", "w") as f:
        self.eff_loss.setVolume(float(value) / 100)
        self.eff_clap.setVolume(float(value) / 100)
        f.write(str(value))


def sm_f(self):
    self.sm = Frame(0, 0, 0, 0, self.centralwidget)

    self.selected_level = 0
    self.max_level = 2
    self.list_song = ["Симфония №1", "Надежда", "Уровень №3"]
    self.list_singer = ["si7ence", "si7ence ", " "]

    self.bg_sm = LabelPng("design/sm/bg.png", 0, 0, 1920, 1080, self.sm)
    self.score_field_sm = LabelPng("design/sm/score_field.png", 35, 40, 700, 1000, self.sm)
    self.arrow_up = PushButton("design/sm/arrow_up.png", "design/sm/arrow_up.png", 1349, 148, 116, 100, self.sm)
    self.central_field_sm = PushButton("design/sm/central_field.png", "design/sm/central_field.png", 894, 300, 1026, 195, self.sm)
    self.arrow_down = PushButton("design/sm/arrow_down.png", "design/sm/arrow_down.png", 1352, 547, 110, 100, self.sm)
    self.sm_goto_mm = PushButton("design/sm/goto_mm.png", "design/sm/goto_mm_s.png", 1109, 915, 760, 121, self.sm)

    self.song = LabelText(font2, 920, 270, 350, 195, 241, 188, 65, self.list_song[self.selected_level], self.sm)
    self.singer = LabelText(font3, 930, 330, 300, 195, 241, 188, 65, self.list_singer[self.selected_level], self.sm)


def lvl_f(self):
    self.lvl = Frame(0, 0, 0, 0, self.centralwidget)

    skin_txt = open("text/skins.txt")
    skin = skin_txt.read()
    skin_txt.close()

    self.bg_lvl = LabelPng("design/skins/" + skin + "/bg.png", 0, 0, 1920, 1080, self.lvl)

    self.accuracy_lbl = LabelText(font2, 30, 900, 221, 71, 79, 246, 247, "Точность", self.lvl)
    self.score_lbl = LabelText(font1, 1470, 10, 161, 71, 79, 246, 247, "Счёт:", self.lvl)
    self.combo_lbl = LabelText(font1, 1560, 60, 231, 91, 79, 246, 247, "Комбо x", self.lvl)

    if accuracy_num == 100:
        self.accuracy_tx = LabelText(font2, 70, 970, 81, 71, 79, 246, 247, accuracy_num, self.lvl)
        self.accuracy_pct = LabelText(font2, 160, 970, 51, 71, 79, 246, 247, "%", self.lvl)
    else:
        self.accuracy_tx = LabelText(font2, 80, 970, 81, 71, 79, 246, 247, accuracy_num, self.lvl)
        self.accuracy_pct = LabelText(font2, 150, 970, 51, 71, 79, 246, 247, "%", self.lvl)

    self.score_tx = LabelText(font2, 1630, 15, 271, 71, 79, 246, 247, score_num, self.lvl)
    self.combo_tx = LabelText(font2, 1790, 80, 101, 61, 79, 246, 247, combo_num, self.lvl)
    self.music_name = LabelText(font3, 20, 20, 461, 61, 79, 246, 247, self.list_song[self.selected_level], self.lvl)
    self.singer_name = LabelText(font4, 30, 60, 311, 61, 79, 246, 247, self.list_singer[self.selected_level], self.lvl)

    self.lvl_1 = Frame(0, 0, 0, 0, self.lvl)
    self.lvl_2 = Frame(0, 0, 0, 0, self.lvl)
    self.lvl_3 = Frame(0, 0, 0, 0, self.lvl)
    self.bg_will_be_later = self.bg_sm = LabelPng("design/sm/bg.png", 0, 0, 0, 0, self.lvl_3)
    self.will_be_later = LabelText(font1, 0, 0, 0, 0, 21, 59, 71, "Будет позже", self.lvl_3)

    #все фигуры
    #круг
    self.lc_1 = LabelPng("design/skins/" + skin + "/circle.png", 0, 0, 0, 0, self.lvl_1)
    self.lc_2 = LabelPng("design/skins/" + skin + "/circle.png", 0, 0, 0, 0, self.lvl_1)
    self.lc_3 = LabelPng("design/skins/" + skin + "/circle.png", 0, 0, 0, 0, self.lvl_1)
    self.lc_4 = LabelPng("design/skins/" + skin + "/circle.png", 0, 0, 0, 0, self.lvl_1)
    self.lc_5 = LabelPng("design/skins/" + skin + "/circle.png", 0, 0, 0, 0, self.lvl_1)
    #квадрат
    self.ls_start_1 = LabelPng("design/skins/" + skin + "/square.png", 0, 0, 0, 0, self.lvl_1)
    self.ls_end_1 = LabelPng("design/skins/" + skin + "/square.png", 0, 0, 0, 0, self.lvl_1)
    self.ls_start_2 = LabelPng("design/skins/" + skin + "/square.png", 0, 0, 0, 0, self.lvl_1)
    self.ls_end_2 = LabelPng("design/skins/" + skin + "/square.png", 0, 0, 0, 0, self.lvl_1)
    self.ls_start_3 = LabelPng("design/skins/" + skin + "/square.png", 0, 0, 0, 0, self.lvl_1)
    self.ls_end_3 = LabelPng("design/skins/" + skin + "/square.png", 0, 0, 0, 0, self.lvl_1)
    #ромб
    self.lr_1 = LabelPng("design/skins/" + skin + "/rhombus.png", 0, 0, 0, 0, self.lvl_1)

    self.goto_sm = PushButton("design/lvl/goto_sm.png", "design/lvl/goto_sm_s.png", 1739, 909, 121, 121, self.lvl)

def win_f(self):
    self.win = Frame(0, 0, 0, 0, self.centralwidget)
    self.bg_w = LabelPng("design/win/bg.png", 0, 0, 1920, 1080, self.win)
    self.score_field_sm_w = LabelPng("design/win/score_field.png", 35, 40, 700, 1000, self.win)
    self.again_w = PushButton("design/win/again.png", "design/win/again_s.png", 873, 562, 121, 121, self.win)
    self.w_goto_mm = PushButton("design/win/goto_mm.png", "design/win/goto_mm_s.png", 1023, 562, 760, 121, self.win)
    self.w_goto_sm = PushButton("design/win/goto_sm.png", "design/win/goto_sm_s.png", 873, 398, 910, 121, self.win)

def lose_f(self):
    self.lose = Frame(0, 0, 0, 0, self.centralwidget)
    self.bg_l = LabelPng("design/lose/bg.png", 0, 0, 1920, 1080, self.lose)
    self.again_l = PushButton("design/lose/again.png", "design/lose/again_s.png", 505, 562, 121, 121, self.lose)
    self.l_goto_mm = PushButton("design/lose/goto_mm.png", "design/lose/goto_mm_s.png", 655, 562, 760, 121, self.lose)
    self.l_goto_sm = PushButton("design/lose/goto_sm.png", "design/lose/goto_sm_s.png", 505, 398, 910, 121, self.lose)