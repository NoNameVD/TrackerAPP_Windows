from PySide6.QtWidgets import QDialog, QPushButton, QCheckBox
from PySide6.QtGui import QIcon
from styles.setting_dialog_styles import SETTINGS_DIALOG_STYLE
import json
from db_using import clear_db
import os
import winreg
import subprocess
import sys


class SettingsDialog(QDialog):
    def __init__(self, main):
        super().__init__()
        self.setObjectName("Settings")
        self.setWindowTitle("Настройки")
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon('icons/tracker-icon.ico'))

        # Современная темная тема для диалога настроек
        self.setStyleSheet(SETTINGS_DIALOG_STYLE)

        self.reset_data = {"settings": {"auto_start": False}, "hi_window": {"active": False}}
        self.data_settings = {}

        self.auto_start = QCheckBox("Авто-старт трекера", self)
        self.auto_start.setGeometry(20, 20, 200, 30)

        with open("configs/config.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            self.data_settings = data
        if data["settings"]["auto_start"] == True:
            self.auto_start.setChecked(True)

        self.reset_app = QPushButton("Сбросить", self)
        self.reset_app.setObjectName("reset_app")
        self.reset_app.setGeometry(20, 260, 100, 30)
        self.reset_app.clicked.connect(self.reset_settings)

        self.reset_db = QPushButton("Очистить историю", self)
        self.reset_db.setObjectName("reset_db")
        self.reset_db.setGeometry(20, 60, 160, 30)

        def clear_all():
            os.system("taskkill /f /im tracker.exe")
            clear_db()
            subprocess.Popen(["tracker.exe"])
            main.ui.state_tracker.setText("Трекер запущен")
            main.ui.state_tracker.setGeometry(790, 10, 100, 40)
            main.ui.start_tracker.setEnabled(False)
            main.ui.start_tracker.setVisible(False)

        self.reset_db.clicked.connect(clear_all)

        self.btn_ok = QPushButton("Сохранить", self)
        self.btn_ok.setObjectName("btn_ok")
        self.btn_ok.setGeometry(200, 260, 95, 30)

        self.btn_cancel = QPushButton("Закрыть", self)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.setGeometry(300, 260, 95, 30)

        self.btn_ok.clicked.connect(self.save_file)
        self.btn_cancel.clicked.connect(self.reject)
        self.auto_start.clicked.connect(self.update_settings)

    def save_file(self):
        with open("configs/config.json", "w", encoding="utf-8") as f:
            json.dump(self.data_settings, f, indent=4)
        self.accept()

    def update_settings(self):
        self.data_settings["settings"]["auto_start"] = self.auto_start.isChecked()
        if self.auto_start.isChecked():
            self.add_to_autorun("tracker")
        else:
            self.remove_from_autorun("tracker")

    def reset_settings(self):
        self.data_settings["settings"]["auto_start"] = False
        self.data_settings["hi_window"]["active"] = False
        self.auto_start.setChecked(False)

    def add_to_autorun(self, app_name: str):
        current_folder = os.path.dirname(sys.executable)
        exe_path = os.path.join(current_folder, "tracker.exe")

        reg_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )

        winreg.SetValueEx(reg_key, app_name, 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(reg_key)

    def remove_from_autorun(self, app_name: str):
        reg_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        try:
            winreg.DeleteValue(reg_key, app_name)
        except FileNotFoundError:
            pass
        winreg.CloseKey(reg_key)