# -*- coding: utf-8 -*-
"""Всплывающее окно с информацией."""

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox


def message_info(
    icon: QIcon,
    text: str,
    title: str
) -> None:
    """Вызывает всплывающее окно с переданным сообщением.

    Args:
        icon (QIcon): Иконка в заголовке окна.
        text (str): Текст сообщения.
        title (str): Текст в заголовке окна.
    """
    window = QMessageBox()
    window.setIcon(QMessageBox.Icon.Information)
    window.setText(text)
    window.setWindowIcon(icon)
    window.setWindowTitle(title)
    window.exec()
