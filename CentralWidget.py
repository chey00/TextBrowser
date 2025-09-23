from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QTextBrowser, QVBoxLayout, QGridLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__push_button_append = QPushButton("Hinzufügen")
        self.__push_button_append.clicked.connect(self.append)

        self.__push_button_text = QPushButton("set_text")
        self.__push_button_text.clicked.connect(self.set_text)

        self.__push_button_clear = QPushButton("Text löschen")
        self.__push_button_clear.clicked.connect(self.clear)

        self.__push_button_backward = QPushButton("Zurück")
        self.__push_button_backward.clicked.connect(self.backward)

        self.__line_edit = QLineEdit()

        self.__text_browser = QTextBrowser()
        self.__text_browser.setUndoRedoEnabled(True)

        layout = QGridLayout()
        layout.addWidget(self.__line_edit, 0, 0, 1, 2)
        layout.addWidget(self.__push_button_append, 1, 0)
        layout.addWidget(self.__push_button_text, 1, 1)
        layout.addWidget(self.__push_button_clear, 2, 0)
        layout.addWidget(self.__push_button_backward, 2, 1)
        layout.addWidget(self.__text_browser, 3, 0, 1, 2)

        self.setLayout(layout)

    @pyqtSlot()
    def append(self):
        text = self.__line_edit.text()

        self.__text_browser.append(text)

    @pyqtSlot()
    def set_text(self):
        text = self.__line_edit.text()

        self.__text_browser.setText(text)

    @pyqtSlot()
    def clear(self):
        self.__text_browser.clear()

    @pyqtSlot()
    def backward(self):
        self.__text_browser.undo()
