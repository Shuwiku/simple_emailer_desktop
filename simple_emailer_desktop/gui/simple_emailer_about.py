# -*- coding: utf-8 -*-
"""Окно с информацией о приложении."""

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget

from .forms import Ui_FormSimpleEmailerAbout


class SimpleEmailerAbout(
    QWidget,
    Ui_FormSimpleEmailerAbout
):
    """Окно с информацией о приложении."""

    # Иконка в заголовке окна
    icon: QIcon

    def __init__(
        self,
        icon: QIcon
    ) -> None:
        """Инициализация и настройка окна."""
        super().__init__()

        self.icon = icon

        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowIcon(self.icon)

        self._setup()

    def _setup(self) -> None:
        """Настраивает отображение элементов в окне."""
        self.button_close.clicked.connect(
            slot=(lambda: self.close())
        )
        self.label_icon.setPixmap(self.icon.pixmap(91, 91))
