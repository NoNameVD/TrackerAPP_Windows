from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QDialog, QLabel, QCheckBox
from PySide6.QtGui import QIcon, QPixmap
from styles.hi_window_styles import HI_WINDOW_STYLE
import json


class hi_window(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("hi_window")
        self.setWindowTitle("Начало работы")
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon('icons/tracker-icon.ico'))

        # Современная темная тема для приветственного окна
        self.setStyleSheet(HI_WINDOW_STYLE)

        self.data_hiwindow = {}

        self.label = QLabel(self)
        self.pixmap = QPixmap("icons/tracker-icon.ico")

        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setGeometry(165, 40, 70, 70)

        self.label_info = QLabel(
            "Beta версия приложения TrackerAPP.\nДля корректной работы следует\nперевести трекер в режим автозапуска",
            self)
        self.label_info.setObjectName("label_info")
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_info.setGeometry(0, 100, 400, 80)

        self.button_settings = QPushButton("Настройки", self)
        self.button_settings.setObjectName("button_settings")
        self.button_settings.clicked.connect(lambda: self.save_settings("settings"))
        self.button_settings.setGeometry(150, 180, 100, 30)

        self.load_settings()

        self.check = QCheckBox("Больше не показывать", self)
        self.check.setGeometry(125, 220, 160, 30)
        self.check.clicked.connect(self.update_settings)

        self.button_ok = QPushButton("OK", self)
        self.button_ok.setObjectName("button_ok")
        self.button_ok.clicked.connect(lambda: self.save_settings('ok'))
        self.button_ok.setGeometry(340, 255, 40, 35)

    def save_settings(self, why: str):
        with open('configs/config.json', 'w', encoding='utf-8') as f:
            json.dump(self.data_hiwindow, f, indent=4)
        if why == "settings":
            self.accept()
        else:
            self.reject()

    def load_settings(self):
        with open("configs/config.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            self.data_hiwindow = data

    def update_settings(self):
        self.data_hiwindow["hi_window"]["active"] = self.check.isChecked()