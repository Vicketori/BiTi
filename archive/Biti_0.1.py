import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Game_2 import Ui_Game


"""taskbar icon"""
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_Game()
ui.setupUi(window)
window.showFullScreen()
sys.exit(app.exec())

""" уровень перерисовать """
#анимация фона
#зажатие кнопок на время или по количество какого-то достижения
#хранить рекорды 3шт(макс.счёт, макс.комбо, макс.точность) и выбранный скин в TXT
#(баги) при нажатии прекратить уровень > вывести проигрыш > при начале заново всё сначала
#создать коробку для хранения страниц(слайдов)