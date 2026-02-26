from datetime import datetime
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QScrollArea, QWidget, QSpacerItem, QSizePolicy, QLabel
from PySide6.QtCore import Qt, QSize
from styles.detail_activity_dialog_styles import DETAIL_ACTIVITY_DIALOG_STYLE, ACTIVITY_ITEM_STYLE
from db_using import get_detail_activity


class DetailActivityDialog(QDialog):
    def __init__(self, id_session: int, process_name: str):
        super().__init__()
        self.setObjectName("DetailActivity")
        self.detail_activity = get_detail_activity(id_session, process_name)
        self.setWindowTitle(f'Дополнительная информация о "{process_name}"')
        self.setFixedSize(840, 460)
        self.setWindowIcon(QIcon('icons/tracker-icon.ico'))

        # Современная темная тема для диалога детальной активности
        self.setStyleSheet(DETAIL_ACTIVITY_DIALOG_STYLE)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setGeometry(0, 0, 840, 460)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scrollContents = QWidget()
        self.scrollContents.setObjectName("scrollContents")
        self.scrollArea.setWidget(self.scrollContents)

        self.layout = QVBoxLayout(self.scrollContents)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)

        for elem in self.detail_activity:
            item = self.create_item(elem[2], elem[3], elem[4])
            self.layout.addWidget(item)

        self.spacer = self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def create_item(self, process_name: str, time_start_text: str, time_end_text: str):
        item = QWidget(self.scrollContents)
        item.setFixedSize(800, 60)
        item.setObjectName("ActivityItem")

        item.setStyleSheet(ACTIVITY_ITEM_STYLE)

        # Процесс:
        why_name = QLabel("Процесс:", item)
        why_name.setObjectName("label_header")
        why_name.setGeometry(10, 5, 70, 22)

        name_label = QLabel(process_name, item)
        name_label.setObjectName("name_label")
        name_label.setGeometry(10, 27, 180, 28)
        name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Начало:
        why_time_start = QLabel("Начало:", item)
        why_time_start.setObjectName("label_header")
        why_time_start.setGeometry(200, 5, 60, 22)

        time_start_label = QLabel(time_start_text, item)
        time_start_label.setObjectName("label_value")
        time_start_label.setGeometry(200, 27, 130, 28)
        time_start_label.setAlignment(Qt.AlignCenter)

        # Конец:
        why_time_end = QLabel("Конец:", item)
        why_time_end.setObjectName("label_header")
        why_time_end.setGeometry(340, 5, 55, 22)

        time_end_label = QLabel(time_end_text, item)
        time_end_label.setObjectName("label_value")
        time_end_label.setGeometry(340, 27, 130, 28)
        time_end_label.setAlignment(Qt.AlignCenter)

        # Общее время:
        time_start = datetime.strptime(time_start_text, "%Y-%m-%d %H:%M:%S")
        time_end = datetime.strptime(time_end_text, "%Y-%m-%d %H:%M:%S")
        duration = (time_end - time_start)

        why_duration = QLabel("Общее время:", item)
        why_duration.setObjectName("label_header")
        why_duration.setGeometry(480, 5, 110, 22)

        duration_label = QLabel(str(duration), item)
        duration_label.setObjectName("duration_label")
        duration_label.setGeometry(480, 27, 120, 28)
        duration_label.setAlignment(Qt.AlignCenter)

        return item