# -*- coding: utf-8 -*-
"""DOCSTRING."""

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget

from .forms import Ui_FormSimpleEmailerAbout


class SimpleEmailerAbout(
    QWidget,
    Ui_FormSimpleEmailerAbout
):
    """DOCSTRING."""

    def __init__(self) -> None:
        """DOCSTRING."""
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.button_close.clicked.connect(
            slot=(lambda: self.close())
        )

        self.label_icon.setPixmap(QPixmap("icon.ico").scaled(91, 91))
