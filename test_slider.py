from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

v = 50
class SliderDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setRange(0, 100)
        self.slider.setValue(v)
        self.slider.setStyleSheet(
            'QSlider:handle:horizontal{width:100px; height:50px; image:url("design/st/handle.png");}')
        self.slider.setPageStep(5)
        # self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.value_changed)

        # Создаем метку для отображения значения слайдера
        self.label = QLabel('50', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def value_changed(self):
        value = self.slider.value()
        self.label.setText(str(value))
        with open('slider_value.txt', 'w') as f:
            f.write(f'{value/100}')
            f.close()



# Запускаем приложение
if __name__ == '__main__':
    app = QApplication([])
    demo = SliderDemo()
    demo.show()
    app.exec()
