from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QTextBrowser, QVBoxLayout, QGridLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__push_button_append = QPushButton("Hinzufügen")
        self.__push_button_append.clicked.connect(self.append)

        self.__push_button_text = QPushButton("set_text")
        self.__push_button_text.clicked.connect(self.set_text)

        self.__line_edit = QLineEdit()
        self.__text_browser = QTextBrowser()

        layout = QGridLayout()
        layout.addWidget(self.__line_edit, 0, 0, 1, 2)
        layout.addWidget(self.__push_button_append, 1, 0)
        layout.addWidget(self.__push_button_text, 1, 1)
        layout.addWidget(self.__text_browser, 2, 0, 1, 2)

        self.setLayout(layout)

    @pyqtSlot()
    def append(self):
        text = self.__line_edit.text()

        self.__text_browser.append(text)

    @pyqtSlot()
    def set_text(self):
        text = self.__line_edit.text()

        self.__text_browser.setText(text)
