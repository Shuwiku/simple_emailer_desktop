# -*- coding: utf-8 -*-
"""DOCSTRING."""

import json
import sys

from PyQt6.QtWidgets import QApplication

from gui import SimpleEmailer


def main() -> None:
    """DOCSTRING."""
    with open("config.json", mode="r", encoding="utf-8") as f:
        config: dict = json.load(f)
    application: ... = QApplication([])
    window: ... = SimpleEmailer(config=config)
    window.show()
    sys.exit(application.exec())


if __name__ == "__main__":
    main()
