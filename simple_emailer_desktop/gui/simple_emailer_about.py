# -*- coding: utf-8 -*-
"""Окно с информацией о приложении."""

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget

from .forms import Ui_FormSimpleEmailerAbout


class SimpleEmailerAbout(
    QWidget,
    Ui_FormSimpleEmailerAbout
):
    """Окно с информацией о приложении."""

    def __init__(self) -> None:
        """Инициализация и настройка окна."""
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon("icon.ico"))

        self._setup()

    def _setup(self) -> None:
        """Настраивает отображение элементов в окне."""
        self.button_close.clicked.connect(
            slot=(lambda: self.close())
        )
        self.label_icon.setPixmap(QPixmap("icon.ico").scaled(91, 91))
