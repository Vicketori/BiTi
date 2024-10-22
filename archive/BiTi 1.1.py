import sys
import ctypes
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QCursor, QFont, QFontDatabase
from PyQt6.QtCore import QSize, QPropertyAnimation, QParallelAnimationGroup, QPoint, QCoreApplication, QMetaObject, QUrl, Qt
from PyQt6.QtMultimedia import QSoundEffect



class Ui_Game(object):
    def setupUi(self, Game):
        self.centralwidget = QWidget(parent=Game)


        def main_menu():
            self.bg_1_mm = QLabel(parent=self.centralwidget)
            self.bg_1_mm.setPixmap(QPixmap("design/bg_1_mm.png"))
            self.bg_1_mm.setGeometry(0, -1750, 1920, 2830)

            # анимация фона
            self.anim_bg_1_mm = QPropertyAnimation(self.bg_1_mm, b"pos")
            self.anim_bg_1_mm.setEndValue(QPoint(0, 0))
            self.anim_bg_1_mm.setDuration(5500)
            self.anim_bg_1_mm.setLoopCount(-2)
            self.anim_bg_1_mm.start()

            self.bg_eff_mm = QLabel(parent=self.centralwidget)
            self.bg_eff_mm.setGeometry(0, 0, 1920, 1080)
            self.bg_eff_mm.setPixmap(QPixmap("design/bg_2_mm.png"))
            self.effect = QSoundEffect()

            self.effect.setSource(QUrl.fromLocalFile("music/main_menu.wav"))
            self.effect.setLoopCount(-2)
            """настройки слайдер"""
            self.effect.setVolume(0.5)
            self.effect.play()

            self.BiTi_lbl_mm = QLabel(parent=self.centralwidget)
            self.BiTi_lbl_mm.setGeometry(607, 124, 734, 422)
            self.BiTi_lbl_mm.setPixmap(QPixmap("design/BiTi_mm.png"))

            self.start_btn_mm = QPushButton(parent=self.centralwidget)
            self.start_btn_mm.setGeometry(580, 618, 760, 121)
            self.start_btn_mm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.start_btn_mm.setStyleSheet("QPushButton {border-radius: 60px}")
            self.start_btn_mm.setIcon(QIcon(QPixmap("design/start_mm.png")))
            self.start_btn_mm.setIconSize(QSize(760, 121))

            #из главного в меню выбора уровня
            # self.start_btn_mm.clicked.connect()

            self.skins_btn_mm = QPushButton(parent=self.centralwidget)
            self.skins_btn_mm.setGeometry(580, 790, 360, 121)
            self.skins_btn_mm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.skins_btn_mm.setStyleSheet("QPushButton {border-radius: 60px}")
            self.skins_btn_mm.setIcon(QIcon(QPixmap("design/skins_mm.png")))
            self.skins_btn_mm.setIconSize(QSize(360, 121))

            self.quit_btn_mm = QPushButton(parent=self.centralwidget)
            self.quit_btn_mm.setGeometry(980, 790, 360, 121)
            self.quit_btn_mm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.quit_btn_mm.setStyleSheet("QPushButton {border-radius: 60px}")
            self.quit_btn_mm.setIcon(QIcon(QPixmap("design/quit_mm.png")))
            self.quit_btn_mm.setIconSize(QSize(360, 121))

            #выход из игры
            self.quit_btn_mm.clicked.connect(app.quit)

            self.settings_btn_mm = QPushButton(parent=self.centralwidget)
            self.settings_btn_mm.setGeometry(1739, 909, 121, 121)
            self.settings_btn_mm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.settings_btn_mm.setStyleSheet("QPushButton {border-radius: 60px}")
            self.settings_btn_mm.setIcon(QIcon(QPixmap("design/settings_mm.png")))
            self.settings_btn_mm.setIconSize(QSize(121, 121))

            Game.setCentralWidget(self.centralwidget)


        def slcm():
            self.bg_slcm = QLabel(parent=self.centralwidget)
            self.bg_slcm.setGeometry(0, 0, 1920, 1080)
            self.bg_slcm.setPixmap(QPixmap("design/bg_slcm.png"))

            self.score_field_slcm = QLabel(parent=self.centralwidget)
            self.score_field_slcm.setGeometry(35, 40, 700, 1000)
            self.score_field_slcm.setPixmap(QPixmap("design/score_field_slcm.png"))

            self.music_bg_field_down_slcm = QLabel(parent=self.centralwidget)
            self.music_bg_field_down_slcm.setGeometry(1000, 525, 1300, 195)
            self.music_bg_field_down_slcm.setPixmap(QPixmap("design/music_bg_field_slcm.png"))

            self.music_bg_field_up_slcm_2 = QLabel(parent=self.centralwidget)
            self.music_bg_field_up_slcm_2.setGeometry(1000, 75, 1300, 195)
            self.music_bg_field_up_slcm_2.setPixmap(QPixmap("design/music_bg_field_slcm.png"))

            self.music_field_center_slcm = QPushButton(parent=self.centralwidget)
            self.music_field_center_slcm.setGeometry(894, 300, 1300, 195)
            self.music_field_center_slcm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.music_field_center_slcm.setStyleSheet("QPushButton {border-radius: 40px}")
            self.music_field_center_slcm.setIcon(QIcon(QPixmap("design/music_center_field_slcm.png")))
            self.music_field_center_slcm.setIconSize(QSize(1300, 195))

            self.goto_mm = QPushButton(parent=self.centralwidget)
            self.goto_mm.setGeometry(1109, 915, 760, 121)
            self.goto_mm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.goto_mm.setStyleSheet("QPushButton {border-radius: 60px}")
            self.goto_mm.setIcon(QIcon(QPixmap("design/goto_mm.png")))
            self.goto_mm.setIconSize(QSize(760, 121))

            Game.setCentralWidget(self.centralwidget)


        def lvl():
            i = 1
            self.bg_lvl = QLabel(parent=self.centralwidget)
            self.bg_lvl.setGeometry(0, 0, 1920, 1080)
            self.bg_lvl.setPixmap(QPixmap("design/skins/"+str(i)+"/bg_lvl.png"))

            self.goto_slcm_lvl = QPushButton(parent=self.centralwidget)
            self.goto_slcm_lvl.setGeometry(1739, 909, 121, 121)
            self.goto_slcm_lvl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.goto_slcm_lvl.setStyleSheet("QPushButton {border-radius: 60px}")
            self.start_btn_mm.setIcon(QIcon(QPixmap("design/goto_slcm_lvl.png")))
            self.goto_slcm_lvl.setIcon(i_goto_slcm_lvl)
            self.goto_slcm_lvl.setIconSize(QSize(121, 121))


            # шрифт 1
            font_1 = QFont()
            font_1.setFamily("Architun")
            font_1.setPointSize(60)

            self.score_lbl_lvl = QLabel(parent=self.centralwidget)
            self.score_lbl_lvl.setGeometry(1470, 10, 161, 71)
            self.score_lbl_lvl.setFont(font_1)
            self.score_lbl_lvl.setStyleSheet("color: rgb(79, 246, 247)")
            self.score_lbl_lvl.setText("Счёт:")

            self.combo_lbl_lvl = QLabel(parent=self.centralwidget)
            self.combo_lbl_lvl.setGeometry(1560, 60, 231, 91)
            self.combo_lbl_lvl.setFont(font_1)
            self.combo_lbl_lvl.setStyleSheet("color: rgb(79, 246, 247)")
            self.combo_lbl_lvl.setText("Комбо x")


            # шрифт 2
            font_2 = QFont()
            font_2.setFamily("Architun")
            font_2.setPointSize(48)

            self.score_num_lvl = QLabel(parent=self.centralwidget)
            self.score_num_lvl.setGeometry(1630, 15, 271, 71)
            self.score_num_lvl.setFont(font_2)
            self.score_num_lvl.setStyleSheet("color: rgb(79, 246, 247)")

            self.combo_num_lvl = QLabel(parent=self.centralwidget)
            self.combo_num_lvl.setGeometry(1790, 80, 101, 61)
            self.combo_num_lvl.setFont(font_2)
            self.combo_num_lvl.setStyleSheet("color: rgb(79, 246, 247)")

            self.accuracy_lbl_lvl = QLabel(parent=self.centralwidget)
            self.accuracy_lbl_lvl.setGeometry(30, 900, 221, 71)
            self.accuracy_lbl_lvl.setFont(font_2)
            self.accuracy_lbl_lvl.setStyleSheet("color: rgb(79, 246, 247)")
            self.accuracy_lbl_lvl.setText("точность")

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
            self.score_num_lvl.setText(score)
            self.combo_num_lvl.setText(combo)
            self.accuracy_num.setText(accuracy)
            self.music.setText(music_name)
            self.singer.setText(singer_name)

            Game.setCentralWidget(self.centralwidget)







        main_menu()
        # slcm()
        # lvl()



app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_Game()
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
sys.exit(app.exec())