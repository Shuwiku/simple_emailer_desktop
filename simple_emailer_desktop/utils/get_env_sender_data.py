# -*- coding: utf-8 -*-
"""Получает адрес почты и пароль отправителя из переменных окружения."""

import os
from typing import Optional

from dotenv import load_dotenv


def get_env_sender_data() -> tuple[str, str]:
    """Получает адрес почты и пароль отправителя из переменных окружения.

    Raises:
        ValueError: Если адрес почты или пароль отсутствуют в переменных
            окружения.

    Returns:
        tuple[str, str]: Адрес почты и пароль отправителя.
    """
    load_dotenv()

    sender_email: Optional[str] = os.getenv("SENDER_EMAIL")
    sender_password: Optional[str] = os.getenv("SENDER_PASSWORD")

    if sender_email is None or sender_password is None:
        raise ValueError("Адрес почты или пароль отсутствуют в"
                         " переменных окружения.")

    return sender_email, sender_password
