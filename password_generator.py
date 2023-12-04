import random
import string
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()
        # ставлю фиксированный размер окна программы
        self.setFixedSize(400, 300)  
        # Создание кнопки
        self.button = QPushButton('Generate', self)

        # Подключение события клика по кнопке к методу
        self.button.clicked.connect(self.on_button_click)

        # Создание метки для вывода текста
        self.label = QLabel('', self)
        self.label.setStyleSheet("""
            QLabel {
                font-size: 14px;
            }
        """)

        # Вторая строка для отображения
        self.second_line = ''

        # Делаем метку "кликабельной" и устанавливаем отслеживание клика
        self.label.setOpenExternalLinks(True)
        self.label.mousePressEvent = self.on_label_click

        # Включаем отслеживание движения мыши для метки
        self.label.setMouseTracking(True)
        # Подключаем событие входа мыши на метку к методу
        self.label.enterEvent = self.on_label_enter

        # Создание макета и добавление кнопки и метки на виджет
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        # Установка макета для основного виджета
        self.setLayout(layout)

    def on_button_click(self):
        # Метод, который будет вызываться при клике по кнопке
        def generate_random_string(length):
            characters = string.ascii_letters + string.digits
            return ''.join(random.choice(characters) for _ in range(length))

        # Пример использования: генерация случайной строки длиной 16 символов
        random_string = generate_random_string(16)
        self.second_line = random_string
        self.label.setText(f'Click on the text. It will be copied to the clipboard.\n Your passwprd : {self.second_line}')

    def on_label_click(self, event):
        # Метод, который будет вызываться при клике на метке
        if event.button() == Qt.LeftButton:
            # Копирование только сгенерированного пароля в буфер обмена
            QApplication.clipboard().setText(self.second_line)

    def on_label_enter(self, event):
        # Метод, который будет вызываться при входе мыши на метку
        self.label.setCursor(QCursor(Qt.PointingHandCursor))

if __name__ == '__main__':
    # Создание экземпляра приложения
    app = QApplication(sys.argv)

    # Создание экземпляра приложения
    my_app = MyApplication()

    # Отображение приложения
    my_app.show()

    # Запуск цикла событий
    sys.exit(app.exec_())