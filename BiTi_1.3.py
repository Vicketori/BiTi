import sys
import ctypes
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QCursor, QFont, QFontDatabase
from PyQt6.QtCore import QSize, QPropertyAnimation, QPoint, QUrl, Qt
from PyQt6.QtMultimedia import QSoundEffect


def HCursor(self):
    self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))


def BRadius(self):
    self.setStyleSheet("QPushButton {border-radius: 60 px}")


class PushButton(QPushButton):
    def __init__(self, a, b, w, h, parent=None):
        super(PushButton, self).__init__(parent)

        self.icon_1 = QIcon()
        self.icon_1.addPixmap(QPixmap(a))
        self.setIconSize(QSize(w, h))
        self.setIcon(self.icon_1)

        self.icon_2 = QIcon()
        self.icon_2.addPixmap(QPixmap(b))
        self.setIconSize(QSize(w, h))

    def enterEvent(self, event):
        self.setIcon(self.icon_2)
    def leaveEvent(self, event):
        self.setIcon(self.icon_1)


class Game_(object):
    def setupUi(self, Game):
        self.centralwidget = QWidget(parent=Game)
        Game.setCentralWidget(self.centralwidget)

        """главное меню"""
        self.mm = QFrame(parent=self.centralwidget)
        self.mm.setGeometry(0, 0, 1920, 1080)

        self.bg_mm = QLabel(parent=self.mm)
        self.bg_mm.setPixmap(QPixmap("design/mm/bg_1.png"))
        self.bg_mm.setGeometry(0, -1750, 1920, 2830)

        # анимация фона
        self.anim = QPropertyAnimation(self.bg_mm, b"pos")
        self.anim.setEndValue(QPoint(0, 0))
        self.anim.setDuration(5500)
        self.anim.setLoopCount(-2)
        self.anim.start()

        self.bg_mmef = QLabel(parent=self.mm)
        self.bg_mmef.setGeometry(0, 0, 1920, 1080)
        self.bg_mmef.setPixmap(QPixmap("design/mm/bg_2.png"))

        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("music/main_menu.wav"))
        self.effect.setLoopCount(-2)
        """настройки слайдер"""
        self.effect.setVolume(0.5)
        self.effect.play()

        self.BiTi = QLabel(parent=self.mm)
        self.BiTi.setGeometry(607, 124, 734, 422)
        self.BiTi.setPixmap(QPixmap("design/mm/BiTi.png"))

        self.start = PushButton("design/mm/start.png", "design/mm/start_selected.png", 760, 121, self.mm)
        HCursor(self.start)
        BRadius(self.start)
        self.start.setGeometry(580, 618, 760, 121)

        self.skins = PushButton("design/mm/skins.png", "design/mm/skins_selected.png", 360, 121, self.mm)
        HCursor(self.skins)
        BRadius(self.skins)
        self.skins.setGeometry(580, 790, 360, 121)

        self.quit = PushButton("design/mm/quit.png", "design/mm/quit_selected.png", 360, 121, self.mm)
        HCursor(self.quit)
        BRadius(self.quit)
        self.quit.setGeometry(980, 790, 360, 121)

        self.settings = PushButton("design/mm/settings.png", "design/mm/settings_selected.png", 121, 121, self.mm)
        HCursor(self.settings)
        BRadius(self.settings)
        self.settings.setGeometry(1739, 909, 121, 121)


        """меню выбора"""
        self.slcm = QFrame(parent=self.centralwidget)
        self.slcm.setGeometry(0, 0, 0, 0)

        self.bg_slcm = QLabel(parent=self.slcm)
        self.bg_slcm.setGeometry(0, 0, 1920, 1080)
        self.bg_slcm.setPixmap(QPixmap("design/slcm/bg.png"))

        self.score_field_slcm = QLabel(parent=self.slcm)
        self.score_field_slcm.setGeometry(35, 40, 700, 1000)
        self.score_field_slcm.setPixmap(QPixmap("design/score_field.png"))

        self.music_bg_field_down_slcm = QLabel(parent=self.slcm)
        self.music_bg_field_down_slcm.setGeometry(1000, 525, 950, 195)
        self.music_bg_field_down_slcm.setPixmap(QPixmap("design/slcm/music_field.png"))

        self.music_bg_field_up_slcm_2 = QLabel(parent=self.slcm)
        self.music_bg_field_up_slcm_2.setGeometry(1000, 75, 950, 195)
        self.music_bg_field_up_slcm_2.setPixmap(QPixmap("design/slcm/music_field.png"))

        self.music_field_center_slcm = PushButton("design/slcm/music_center_field.png", "design/slcm/music_center_field.png", 1026, 195, self.slcm)
        HCursor(self.music_field_center_slcm)
        self.music_field_center_slcm.setStyleSheet("QPushButton {border-radius: 40px}")
        self.music_field_center_slcm.setGeometry(894, 300, 1026, 195)

        self.goto = PushButton("design/goto_mm.png","design/goto_mm.png", 760, 121, self.slcm)
        HCursor(self.goto)
        BRadius(self.goto)
        self.goto.setGeometry(1109, 915, 760, 121)
        """добавить кнопки вверх и вниз на лкм"""


        # из главного в меню выбора уровня
        self.start.clicked.connect(self.mm_slcm)

        # из меню выбора в главное меню
        self.goto.clicked.connect(self.slcm_mm)

        # выход из игры
        self.quit.clicked.connect(app.quit)

    def mm_slcm(self):
        self.mm.setGeometry(0, 0, 0, 0)
        self.slcm.setGeometry(0, 0, 1920, 1080)

    def slcm_mm(self):
        self.slcm.setGeometry(0, 0, 0, 0)
        self.mm.setGeometry(0, 0, 1920, 1080)


        def lvl():
            self.bg_lvl = QLabel(parent=self.centralwidget)
            self.bg_lvl.setGeometry(0, 0, 1920, 1080)

            #i - номер скина
            """сохранять и импортировать из/в TXT"""
            i = 1
            self.bg_lvl.setPixmap(QPixmap("design/skins/"+str(i)+"/bg_lvl.png"))

            self.goto_slcm = QPushButton(parent=self.centralwidget)
            self.goto_slcm.setGeometry(1739, 909, 121, 121)
            HCursor(self.goto_slcm)
            BRadius(self.goto_slcm)
            Icon(self.goto_slcm, "design/lvl/goto_slcm.png")
            self.goto_slcm.setIconSize(QSize(121, 121))


            # шрифт 1
            font_1 = QFont()
            font_1.setFamily("Architun")
            font_1.setPointSize(60)

            self.score_lbl = QLabel(parent=self.centralwidget)
            self.score_lbl.setGeometry(1470, 10, 161, 71)
            self.score_lbl.setFont(font_1)
            self.score_lbl.setStyleSheet("color: rgb(79, 246, 247)")
            self.score_lbl.setText("Счёт:")

            self.combo_lbl = QLabel(parent=self.centralwidget)
            self.combo_lbl.setGeometry(1560, 60, 231, 91)
            self.combo_lbl.setFont(font_1)
            self.combo_lbl.setStyleSheet("color: rgb(79, 246, 247)")
            self.combo_lbl.setText("Комбо x")


            # шрифт 2
            font_2 = QFont()
            font_2.setFamily("Architun")
            font_2.setPointSize(48)

            self.score_num = QLabel(parent=self.centralwidget)
            self.score_num.setGeometry(1630, 15, 271, 71)
            self.score_num.setFont(font_2)
            self.score_num.setStyleSheet("color: rgb(79, 246, 247)")

            self.combo_num = QLabel(parent=self.centralwidget)
            self.combo_num.setGeometry(1790, 80, 101, 61)
            self.combo_num.setFont(font_2)
            self.combo_num.setStyleSheet("color: rgb(79, 246, 247)")

            self.accuracy_lbl = QLabel(parent=self.centralwidget)
            self.accuracy_lbl.setGeometry(30, 900, 221, 71)
            self.accuracy_lbl.setFont(font_2)
            self.accuracy_lbl.setStyleSheet("color: rgb(79, 246, 247)")
            self.accuracy_lbl.setText("точность")

            self.accuracy_pct = QLabel(parent=self.centralwidget)
            self.accuracy_pct.setGeometry(150, 970, 51, 71)
            self.accuracy_pct.setFont(font_2)
            self.accuracy_pct.setStyleSheet("color: rgb(79, 246, 247)")
            self.accuracy_pct.setText("%")

            self.accuracy_num = QLabel(parent=self.centralwidget)
            self.accuracy_num.setGeometry(80, 970, 81, 71)
            self.accuracy_num.setFont(font_2)
            self.accuracy_num.setStyleSheet("color: rgb(79, 246, 247)")


            # шрифт 3
            font_3 = QFont()
            font_3.setFamily("Architun")
            font_3.setPointSize(30)

            self.music = QLabel(parent=self.centralwidget)
            self.music.setGeometry(20, 20, 461, 61)
            self.music.setFont(font_3)
            self.music.setStyleSheet("color: rgb(79, 246, 247)")


            # шрифт 4
            font_4 = QFont()
            font_4.setFamily("Architun")
            font_4.setPointSize(20)

            self.singer = QLabel(parent=self.centralwidget)
            self.singer.setGeometry(30, 60, 311, 61)
            self.singer.setFont(font_4)
            self.singer.setStyleSheet("color: rgb(79, 246, 247)")

            #пока затычка
            a = 25
            score = str(a)
            combo = str(a)
            accuracy = str(a)
            music_name = "название уровня"
            singer_name = "то что под названием уровня"
            self.score_num.setText(score)
            self.combo_num.setText(combo)
            self.accuracy_num.setText(accuracy)
            self.music.setText(music_name)
            self.singer.setText(singer_name)

            Game.setCentralWidget(self.centralwidget)



app = QApplication(sys.argv)
window = QMainWindow()
ui = Game_()
ui.setupUi(window)

#шрифт без установки
QFontDatabase.addApplicationFont("text/Architun.ttf")

#иконка окна
window.setWindowIcon(QIcon(QPixmap("design/icon.png")))

#иконка на панели задач
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window.resize(1920, 1080)
window.setIconSize(QSize(32, 32))
window.setWindowTitle("BiTi")
window.showFullScreen()
app.exec()