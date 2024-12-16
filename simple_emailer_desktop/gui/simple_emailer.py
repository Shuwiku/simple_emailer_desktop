# -*- coding: utf-8 -*-
"""Главное окно приложения."""

import os
import sys
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget
from simple_emailer import send_email_quick

from .forms import Ui_FormSimpleEmailer
from .simple_emailer_about import SimpleEmailerAbout


class SimpleEmailer(
    QWidget,
    Ui_FormSimpleEmailer
):
    """Главное окно приложения."""

    # Конфигурация приложения
    config: dict

    # Абсолютный путь к директории с файлами писем
    email_dir: Path

    def __init__(
        self,
        config: dict
    ) -> None:
        """Инициализация и настройка окна."""
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon("icon.ico"))

        self.config = config
        self.email_dir = Path("emails").resolve()

        self._setup()

    def _about(self) -> None:
        """DOCSTRING."""
        self.window_about = SimpleEmailerAbout()
        self.window_about.show()

    def _exit(self) -> None:
        """Закрывает приложение."""
        sys.exit()

    def _send_email(self) -> None:
        """Отправляет письмо согласно вводу пользователя."""
        if self.check_box_use_env_variables.isChecked():
            load_dotenv()
            sender_email: Optional[str] = os.getenv("SENDER_EMAIL")
            sender_password: Optional[str] = os.getenv("SENDER_PASSWORD")
            if sender_email is None or sender_password is None:
                return None
        else:
            sender_email: str = self.line_edit_sender_email.text()
            sender_password: str = self.line_edit_sender_password.text()

        send_email_quick(
            email_text=self.text_edit_email_text.toPlainText(),
            recipient_email=self.line_edit_recipient_email.text(),
            sender_email=sender_email,
            sender_password=sender_password,
            subject=self.line_edit_email_subject.text(),
            email_type=self.combo_box_email_type.currentText()
        )

    def _set_email_data(self) -> None:
        """Подставляет данные письма выбранного пользователем."""
        email: str = \
            self.list_widget_emails_list.currentItem().text()  # type: ignore
        email_config: dict = self.config["emails"][email]

        with open(
            file=(self.email_dir / email_config["filename"]),
            encoding="utf-8"
        ) as f:
            email_text: str = f.read()

        self.combo_box_email_type.setCurrentText(email_config["type"])
        self.line_edit_email_subject.setText(email_config["subject"])
        self.text_edit_email_text.setPlainText(email_text)

    def _setup(self) -> None:
        """Настраивает отображение элементов в окне."""
        self._setup_emails_list()

        self.button_about.clicked.connect(
            slot=self._about
        )
        self.button_exit.clicked.connect(
            slot=self._exit
        )
        self.button_send_email.clicked.connect(
            slot=self._send_email
        )

        self.check_box_use_env_variables.setChecked(True)
        self.check_box_use_env_variables.clicked.connect(
            slot=self._setup_sender_data
        )

        self.combo_box_email_type.addItems(
            [
                "html",
                "plain",
                "markdown"
            ]
        )

        self.line_edit_sender_email.setEnabled(False)
        self.line_edit_sender_password.setEnabled(False)

    def _setup_emails_list(self) -> None:
        """Настраивает список писем на основе данных из файла конфигурации."""
        emails: list = list(self.config["emails"].keys())
        emails.remove("_default")

        for i in emails:
            self.list_widget_emails_list.addItem(i)

        self.list_widget_emails_list.doubleClicked.connect(
            slot=self._set_email_data
        )

    def _setup_sender_data(self) -> None:
        """Настаивает поля с почтой и паролем отправителя."""
        is_enabled: bool = not self.check_box_use_env_variables.isChecked()
        self.line_edit_sender_email.setEnabled(is_enabled)
        self.line_edit_sender_password.setEnabled(is_enabled)
