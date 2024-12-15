# -*- coding: utf-8 -*-
"""Simple Emailer Desktop - утилита для отправки писем через SMTP Gmail."""

import json
import sys
from typing import Final

from PyQt6.QtWidgets import QApplication

from gui import SimpleEmailer


def main() -> None:
    """If __name__ == "__main__"."""
    with open("config.json", mode="r", encoding="utf-8") as f:
        config: dict = json.load(f)

    application: Final = QApplication([])

    window: Final = SimpleEmailer(config=config)
    window.show()

    sys.exit(application.exec())


if __name__ == "__main__":
    main()
