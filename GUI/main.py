from datetime import timedelta, datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel
from window.main_window import Ui_MainWindow
from window.setting_dialog import SettingsDialog
from window.hi_window import hi_window
from db_using import get_all_session, get_all_activity, current_session
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.settings.clicked.connect(self.open_settings)
        self.ui.comboBox.currentIndexChanged.connect(self.select_combobox)

        if self.load_settings() != True:
            _hi_window = hi_window()
            result_hi = _hi_window.exec()

            if result_hi == QDialog.Accepted:
                self.open_settings()

        self.load_combobox()
        self.ui.update_button.clicked.connect(self.load_combobox)

    def load_combobox(self):
        self.ui.comboBox.clear()
        for elem in get_all_session():
            self.ui.add_combobox_item(f"{elem[1]}-{elem[2]}", elem[0])

    def open_settings(self):
        window = SettingsDialog(self)
        window.exec()

    def select_combobox(self):
        self.ui.clear_layout(self.ui.layout)
        id_session = self.ui.comboBox.currentData()
        all_activity = get_all_activity(id_session)
        session = current_session(id_session)

        if session != None:
            duration = "Нет информации"
            if session[1] != None:
                start_time = datetime.strptime(session[0], "%Y-%m-%d %H:%M:%S")
                end_time = datetime.strptime(session[1], "%Y-%m-%d %H:%M:%S")
                duration = str(end_time - start_time)

            self.ui.clear_layout(self.ui.HLayoutBaseInfo)

            # Номер сессии (отдельно, как заголовок)
            label_session_number = QLabel(f"№ {id_session}")
            label_session_number.setObjectName("session_number")
            self.ui.HLayoutBaseInfo.addWidget(label_session_number, 0)

            # Время начала
            label_start_header = QLabel("Время начала:")
            label_start_header.setObjectName("label_header")
            self.ui.HLayoutBaseInfo.addWidget(label_start_header, 0)

            label_start_value = QLabel(session[0])
            label_start_value.setObjectName("label_value")
            self.ui.HLayoutBaseInfo.addWidget(label_start_value, 0)

            # Время конца
            label_end_header = QLabel("Время конца:")
            label_end_header.setObjectName("label_header")
            self.ui.HLayoutBaseInfo.addWidget(label_end_header, 0)

            label_end_value = QLabel("Нет информации" if session[1] == None else session[1])
            label_end_value.setObjectName("label_value")
            self.ui.HLayoutBaseInfo.addWidget(label_end_value, 0)

            # Длительность
            label_duration_header = QLabel("Длительность:")
            label_duration_header.setObjectName("label_header")
            self.ui.HLayoutBaseInfo.addWidget(label_duration_header, 0)

            label_duration_value = QLabel(duration)
            label_duration_value.setObjectName("label_value")
            self.ui.HLayoutBaseInfo.addWidget(label_duration_value, 0)

        for elem in all_activity:
            time = timedelta(seconds=elem[1])
            self.ui.add_item(elem[0], str(time))

    def load_settings(self):
        with open("configs/config.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data["hi_window"]["active"]

app = QApplication([])
window = MainWindow()
window.show()
app.exec()