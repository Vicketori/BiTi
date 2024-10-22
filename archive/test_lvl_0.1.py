# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt6.QtGui import QPixmap, QPainter, QFont
# from PyQt6.QtCore import Qt, QTimer
#
# class BiTiGame(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("BiTi")
#         self.setGeometry(0, 0, 1920, 1080)
#         self.setFixedSize(1920, 1080)
#
#         self.circle_x = 50
#         self.square_x = 300
#         self.y = 500
#         self.speed = 5
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_game)
#         self.timer.start(15)
#
#         self.label = QLabel(self)
#         self.label.setGeometry(500, 100, 200, 100)
#         self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         font = QFont("Arial", 20)
#         self.label.setFont(font)
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#
#         circle_img = QPixmap("design/skins/1/circle.png")
#         square_img = QPixmap("design/skins/1/square.png")
#
#         painter.drawPixmap(self.circle_x, self.y, circle_img)
#         painter.drawPixmap(self.square_x, self.y, square_img)
#
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key.Key_W:
#             if self.square_x - 30 <= self.circle_x <= self.square_x + 30:
#                 self.label.setText("Perfect!")
#             else:
#                 self.label.setText("Miss!")
#
#     def update_game(self):
#         self.circle_x += self.speed
#         if self.circle_x > 1920:
#             self.circle_x = 0
#         self.update()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     biTiGame = BiTiGame()
#     biTiGame.show()
#     sys.exit(app.exec())


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt, QTimer


class BiTiGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BiTi")
        self.setGeometry(0, 0, 1920, 1080)
        self.setFixedSize(1920, 1080)

        self.circle_x = 50
        self.square_x = 300
        self.y = 500
        self.speed = 5

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(15)

        self.label = QLabel(self)
        self.label.setGeometry(500, 100, 200, 100)

    def paintEvent(self, event):
        painter = QPainter(self)

        circle_img = QPixmap("design/skins/1/circle.png")
        square_img = QPixmap("design/skins/1/square.png")

        painter.drawPixmap(self.circle_x, self.y, circle_img)
        painter.drawPixmap(self.square_x, self.y, square_img)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_W:
            if self.square_x - 30 <= self.circle_x <= self.square_x + 30:
                self.label.setText("Perfect!")
            else:
                self.label.setText("Miss!")

    def update_game(self):
        self.circle_x += self.speed
        if self.circle_x > 1920:
            self.circle_x = 0
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    biTiGame = BiTiGame()
    biTiGame.show()
    sys.exit(app.exec())