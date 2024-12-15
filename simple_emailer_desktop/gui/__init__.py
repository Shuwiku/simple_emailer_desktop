# -*- coding: utf-8 -*-
"""Графический интерфейс приложения."""

# Это позволяет импортировать класс напрямую из модуля
# Вместо:   from gui.simple_emailer import SimpleEmailer
# Имеем:    from gui import SimpleEmailer
from .simple_emailer import SimpleEmailer  # noqa: F401
