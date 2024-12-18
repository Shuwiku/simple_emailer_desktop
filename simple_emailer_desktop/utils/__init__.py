# -*- coding: utf-8 -*-
"""Вспомогательные функции приложения."""

# Это позволяет импортировать функции напрямую из модуля
# Вместо:   from utils.get_env_sender_data import get_env_sender_data
# Имеем:    from utils import get_env_sender_data
from .get_env_sender_data import get_env_sender_data  # noqa: F401
