import sys
import ctypes
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QFont, QFontDatabase
from PyQt6.QtCore import QSize, QPropertyAnimation, QPoint, QUrl, Qt
from Frames import mm_f, sm_f, lvl_f, st_f
from PyQt6.QtMultimedia import QSoundEffect


class Game_(object):
    def setupUi(self, Game):
        self.centralwidget = QWidget(parent=Game)
        Game.setCentralWidget(self.centralwidget)

        # музыка в главном меню
        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("music/mm.wav"))
        self.effect.setLoopCount(-2)
        volume = open("text/volume.txt")
        v = volume.read()
        volume.close()

        self.effect.setVolume(float(v))
        self.effect.play()

        mm_f(self)
        sm_f(self)
        lvl_f(self)
        st_f(self)

        # из главного в меню выбора уровня
        self.start.clicked.connect(self.mm_sm)
        # из главного в настройки
        self.settings.clicked.connect(self.mm_st)
        # выход из игры
        self.quit.clicked.connect(app.quit)

        # из настроек в главное меню
        self.st_goto_mm.clicked.connect(self.st_mm)

        # из меню выбора в главное меню
        self.sm_goto_mm.clicked.connect(self.sm_mm)
        # меню выбора -> уровень
        self.central_field_sm.clicked.connect(self.sm_lvl)
        # уровень -> меню выбора
        self.goto_sm.clicked.connect(self.lvl_sm)

    def mm_sm(self):
        self.mm.setGeometry(0, 0, 0, 0)
        self.sm.setGeometry(0, 0, 1920, 1080)

    def mm_st(self):
        self.mm.setGeometry(0, 0, 0, 0)
        self.st.setGeometry(0, 0, 1920, 1080)

    def st_mm(self):
        self.st.setGeometry(0, 0, 0, 0)
        self.mm.setGeometry(0, 0, 1920, 1080)

    def sm_mm(self):
        self.sm.setGeometry(0, 0, 0, 0)
        self.mm.setGeometry(0, 0, 1920, 1080)

    def sm_lvl(self):
        self.sm.setGeometry(0, 0, 0, 0)
        self.lvl.setGeometry(0, 0, 1920, 1080)
        self.effect.stop()

    def lvl_sm(self):
        self.lvl.setGeometry(0, 0, 0, 0)
        self.sm.setGeometry(0, 0, 1920, 1080)
        self.effect.play()

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