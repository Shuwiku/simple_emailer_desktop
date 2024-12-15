# -*- coding: utf-8 -*-
"""DOCSTRING."""

import os
from pathlib import Path

from dotenv import load_dotenv
from simple_emailer import send_email_quick
from PyQt6.QtWidgets import QWidget

from .forms import Ui_FormSimpleEmailer


class SimpleEmailer(
    QWidget,
    Ui_FormSimpleEmailer
):
    """DOCSTRING."""

    config: dict

    def __init__(
        self,
        config: dict
    ) -> None:
        """DOCSTRING."""
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.config = config
        self.email_dir: Path = Path("emails").resolve()

        self._setup()

    def _setup(self) -> None:
        """DOCSTRING."""
        self._setup_emails_list()
        self.combo_box_email_type.addItems(
            [
                "html",
                "plain",
                "markdown"
            ]
        )
        self.check_box_use_env_variables.setChecked(True)
        self.check_box_use_env_variables.clicked.connect(
            slot=self._setup_sender_data
        )
        self.line_edit_sender_email.setEnabled(False)
        self.line_edit_sender_password.setEnabled(False)
        self.button_send_email.clicked.connect(
            slot=self._send_email
        )

    def _setup_emails_list(self) -> None:
        """DOCSTRING."""
        emails: list = list(self.config["emails"].keys())
        emails.remove("_default")

        for i in emails:
            self.list_widget_emails_list.addItem(i)

        self.list_widget_emails_list.clicked.connect(
            slot=self._setup_by_email
        )

    def _setup_by_email(self) -> None:
        """DOCSTRING."""
        email = self.list_widget_emails_list.currentItem().text()  # type: ignore
        email_config: dict = self.config["emails"][email]

        with open(
            file=(self.email_dir / email_config["filename"]),
            encoding="utf-8"
        ) as f:
            email_text: str = f.read()

        self.combo_box_email_type.setCurrentText(email_config["type"])
        self.line_edit_email_subject.setText(email_config["subject"])
        self.text_edit_email_text.setPlainText(email_text)

    def _setup_sender_data(self) -> None:
        """DOCSTRING."""
        is_enabled: bool = not self.check_box_use_env_variables.isChecked()
        self.line_edit_sender_email.setEnabled(is_enabled)
        self.line_edit_sender_password.setEnabled(is_enabled)

    def _send_email(self) -> None:
        """DOCSTRING."""
        if self.check_box_use_env_variables.isChecked():
            load_dotenv()
            sender_email: ... = os.getenv("SENDER_EMAIL")
            sender_password: ... = os.getenv("SENDER_PASSWORD")
        else:
            sender_email: str = self.line_edit_sender_email.text()
            sender_password: str = self.line_edit_sender_password.text()
        email_text: str = self.text_edit_email_text.toPlainText()
        recipient_email: str = self.line_edit_recipient_email.text()
        subject: str = self.line_edit_email_subject.text()
        email_type: str = self.combo_box_email_type.currentText()
        send_email_quick(
            email_text=email_text,
            recipient_email=recipient_email,
            sender_email=sender_email,
            sender_password=sender_password,
            subject=subject,
            email_type=email_type
        )
