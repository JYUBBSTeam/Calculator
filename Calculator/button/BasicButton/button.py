
from PyQt5.QtWidgets import QPushButton


class basic_button(QPushButton):

    def __init__(self, character):
        super().__init__()

        self.setText(character)


