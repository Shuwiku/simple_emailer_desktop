# -*- coding: utf-8 -*-
"""Всплывающее окно с ошибкой."""

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox


def message_error(
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
    window.setIcon(QMessageBox.Icon.Critical)
    window.setText(text)
    window.setWindowIcon(icon)
    window.setWindowTitle(title)
    window.exec()
