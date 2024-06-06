from PyQt6.QtWidgets import QFrame, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QCursor
from PyQt6.QtCore import QSize, QPropertyAnimation, QPoint, QUrl, Qt

from Fonts import font1, font2, font3, font4

#пока затычка
score = 9999999
combo = 999
accuracy = 100
music_name = "Название песни цвцфвфвфцв"
singer_name = "Сингер нэйм вцвцвыаквраерк"

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

#главное меню
def mm_f(self):
    self.mm = QFrame(parent=self.centralwidget)
    self.mm.setGeometry(0, 0, 1920, 1080)
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


#меню выбора уровня
def sm_f(self):
    self.sm = QFrame(parent=self.centralwidget)
    self.sm.setGeometry(0, 0, 0, 0)

    self.bg_sm = LabelPng("design/sm/bg.png", 0, 0, 1920, 1080, self.sm)
    self.score_field_sm = LabelPng("design/sm/score_field.png", 35, 40, 700, 1000, self.sm)
    self.arrow_up = PushButton("design/sm/arrow_up.png", "design/sm/arrow_up_s.png", 1000, 525, 950, 195, self.sm)
    self.central_field_sm = PushButton("design/sm/central_field.png", "design/sm/central_field_s.png", 894, 300, 1026, 195, self.sm)
    self.arrow_down = PushButton("design/sm/arrow_down.png", "design/sm/arrow_down_s.png", 1000, 75, 950, 195, self.sm)
    self.sm_goto_mm = PushButton("design/sm/goto_mm.png", "design/sm/goto_mm_s.png", 1109, 915, 760, 121, self.sm)


#уровень
def lvl_f(self):
    self.lvl = QFrame(parent=self.centralwidget)
    self.lvl.setGeometry(0, 0, 0, 0)

    skin = open("text/skin.txt")
    sk = skin.read()
    skin.close()

    class LabelPng(QLabel):
        def __init__(self, a, x, y, w, h, parent=None):
            super(LabelPng, self).__init__(parent)
            self.setGeometry(x, y, w, h)
            self.setPixmap(QPixmap(a))

    self.bg_lvl = LabelPng("design/skins/" + sk + "/bg_lvl.png", 0, 0, 1920, 1080, self.lvl)
    self.goto_sm = PushButton("design/lvl/goto_sm.png", "design/lvl/goto_sm_s.png", 1739, 909, 121, 121, self.lvl)

    self.accuracy_lbl = LabelText(font2, 30, 900, 221, 71, 79, 246, 247, "Точность", self.lvl)
    self.score_lbl = LabelText(font1, 1470, 10, 161, 71, 79, 246, 247, "Счёт:", self.lvl)
    self.combo_lbl = LabelText(font1, 1560, 60, 231, 91, 79, 246, 247, "Комбо x", self.lvl)

    if accuracy == 100:
        self.accuracy_num = LabelText(font2, 70, 970, 81, 71, 79, 246, 247, accuracy, self.lvl)
        self.accuracy_pct = LabelText(font2, 160, 970, 51, 71, 79, 246, 247, "%", self.lvl)
    else:
        self.accuracy_num = LabelText(font2, 80, 970, 81, 71, 79, 246, 247, accuracy, self.lvl)
        self.accuracy_pct = LabelText(font2, 150, 970, 51, 71, 79, 246, 247, "%", self.lvl)

    self.score_num = LabelText(font2, 1630, 15, 271, 71, 79, 246, 247, score, self.lvl)
    self.combo_num = LabelText(font2, 1790, 80, 101, 61, 79, 246, 247, combo, self.lvl)
    self.music = LabelText(font3, 20, 20, 461, 61, 79, 246, 247, music_name, self.lvl)
    self.singer = LabelText(font4, 30, 60, 311, 61, 79, 246, 247, singer_name, self.lvl)


def st_f(self):
    self.st = QFrame(parent=self.centralwidget)
    self.st.setGeometry(0, 0, 0, 0)
    self.bg_lvl = LabelPng("design/st/bg.png", 0, 0, 1920, 1080, self.st)
    self.st_lbl = LabelPng("design/st/settings.png", 460, 344, 1000, 200, self.st)
    self.st_goto_mm = PushButton("design/sm/goto_mm.png", "design/sm/goto_mm_s.png", 41, 52, 760, 121, self.st)