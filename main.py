import sys
import webbrowser
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QFont, QPalette, QColor


class PremiumApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("NotRedact by @ByDog3r")
        self.setGeometry(100, 100, 300, 200)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1E1E1E"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.main_layout = QVBoxLayout()
        self.create_main_buttons()

        self.setLayout(self.main_layout)

    def create_main_buttons(self):
        self.clear_layout()

        buttons = {
            "TikTok": self.show_tiktok_options,
            "Instagram": lambda: self.open_link("https://www.instagram.com"),
            "Facebook": lambda: self.open_link("https://www.facebook.com"),
        }

        for name, action in buttons.items():
            btn = QPushButton(name)
            btn.setFont(QFont("Arial", 14))
            btn.setStyleSheet(
                "background-color: #6200EE; color: white; padding: 10px; border-radius: 5px;"
            )
            btn.clicked.connect(action)
            self.main_layout.addWidget(btn)

    def show_tiktok_options(self):
        self.clear_layout()

        options = {
            "Remover likes": self.run_tiktok_likes_script,
            "Remover seguidores": self.run_tiktok_followers_script,
            "Remover guardados": self.run_tiktok_saves_script,
        }

        for name, action in options.items():
            btn = QPushButton(name)
            btn.setFont(QFont("Arial", 14))
            btn.setStyleSheet(
                "background-color: #FF0050; color: white; padding: 10px; border-radius: 5px;"
            )
            btn.clicked.connect(action)
            self.main_layout.addWidget(btn)

        back_btn = QPushButton("Volver")
        back_btn.setFont(QFont("Arial", 14))
        back_btn.setStyleSheet(
            "background-color: #6200EE; color: white; padding: 10px; border-radius: 5px;"
        )
        back_btn.clicked.connect(self.create_main_buttons)
        self.main_layout.addWidget(back_btn)

    def run_tiktok_likes_script(self):
        subprocess.Popen(
            [sys.executable, "src/tiktok_likes.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def run_tiktok_saves_script(self):
        subprocess.Popen(
            [sys.executable, "src/tiktok_saves.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def run_tiktok_followers_script(self):
        subprocess.Popen(
            [sys.executable, "src/tiktok_followers.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def tiktok_action(self, action):
        print(f"Ejecutando acción: {action}")

    def open_link(self, url):
        webbrowser.open(url)

    def clear_layout(self):
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PremiumApp()
    window.show()
    sys.exit(app.exec())
