# This file is the main entry point for the application.
# It sets up the environment and launches the main window of the application.

import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication

if __package__:
    from .main_window import MainWindow
else:
    project_root = Path(__file__).resolve().parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    from mdl.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
