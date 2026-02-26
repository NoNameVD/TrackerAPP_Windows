from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QCursor, QIcon
from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QComboBox,
    QScrollArea, QVBoxLayout, QSizePolicy, QSpacerItem, QToolButton, QHBoxLayout
)
from window.detail_activity_dialog import DetailActivityDialog
from styles.main_window_styles import (
    MAIN_WINDOW_STYLE, STATE_TRACKER_STYLE_ACTIVE, STATE_TRACKER_STYLE_INACTIVE,
    MAIN_WIDGET_STYLE, COMBOBOX_STYLE, UPDATE_BUTTON_STYLE, SCROLL_AREA_STYLE,
    SCROLL_CONTENTS_STYLE, ITEM_STYLE, BASE_INFO_STYLES
)
import os
import subprocess


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("TrackerAPP")
        MainWindow.setFixedSize(900, 600)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setWindowIcon(QIcon('icons/tracker-icon.ico'))

        # Главный стиль окна с современной темной темой
        MainWindow.setStyleSheet(MAIN_WINDOW_STYLE)

        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self._create_header()
        self._create_main_block()
        self._create_scroll_area()

    def _create_header(self):
        self.settings = QToolButton(self.centralwidget)
        self.settings.setGeometry(15, 10, 40, 40)
        self.settings.setObjectName("settings")
        self.settings.setIcon(QIcon("icons/settings.png"))
        self.settings.setIconSize(QSize(24, 24))

        def start_tracker_func():
            subprocess.Popen('tracker.exe')
            self.state_tracker.setText("Трекер запущен")
            self.state_tracker.setGeometry(790, 10, 100, 40)
            self.start_tracker.setEnabled(False)
            self.start_tracker.setVisible(False)

        def search_state_tracker(process_name):
            # Получаем список всех процессов через tasklist
            output = subprocess.check_output('tasklist', shell=True, text=True)
            return process_name.lower() in output.lower()

        self.state = search_state_tracker('tracker.exe')
        self.state_tracker = QLabel("", self.centralwidget)
        self.state_tracker.setStyleSheet(STATE_TRACKER_STYLE_ACTIVE)

        self.start_tracker = QPushButton("Запустить", self.centralwidget)
        self.start_tracker.setGeometry(790, 10, 100, 40)
        self.start_tracker.setEnabled(False)
        self.start_tracker.setVisible(False)

        self.start_tracker.clicked.connect(start_tracker_func)

        if self.state:
            self.state_tracker.setText("Трекер запущен")
            self.state_tracker.setGeometry(790, 10, 100, 40)
        else:
            self.state_tracker.setText("Трекер не запущен")
            self.state_tracker.setGeometry(680, 10, 150, 40)
            self.state_tracker.setStyleSheet(STATE_TRACKER_STYLE_INACTIVE)
            self.start_tracker.setEnabled(True)
            self.start_tracker.setVisible(True)

    def _create_main_block(self):
        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setGeometry(15, 59, 870, 531)
        self.main_widget.setObjectName("main_widget")

        self.main_widget.setStyleSheet(MAIN_WIDGET_STYLE)

        self.comboBox = QComboBox(self.main_widget)
        self.comboBox.setGeometry(10, 10, 500, 40)
        self.comboBox.setStyleSheet(COMBOBOX_STYLE)

        self.update_button = QToolButton(self.main_widget)
        self.update_button.setIcon(QIcon("icons/refresh.png"))
        self.update_button.setIconSize(QSize(24, 24))
        self.update_button.setGeometry(520, 10, 40, 40)
        self.update_button.setStyleSheet(UPDATE_BUTTON_STYLE)

        self.widget_base_info = QWidget(self.main_widget)
        self.widget_base_info.setGeometry(10, 60, 850, 50)
        self.HLayoutBaseInfo = QHBoxLayout(self.widget_base_info)
        self.widget_base_info.setStyleSheet(BASE_INFO_STYLES)

    def _create_scroll_area(self):
        self.scrollArea = QScrollArea(self.main_widget)
        self.scrollArea.setGeometry(10, 120, 840, 420)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scrollArea.setStyleSheet(SCROLL_AREA_STYLE)

        self.scrollContents = QWidget()
        self.scrollContents.setStyleSheet(SCROLL_CONTENTS_STYLE)
        self.scrollArea.setWidget(self.scrollContents)

        self.layout = QVBoxLayout(self.scrollContents)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.add_spacer = self.layout.addItem(self.spacer)

    def create_item(self, process_name: str, time_text: str):
        item = QWidget(self.scrollContents)
        item.setFixedSize(800, 50)
        item.setObjectName("Item")

        item.setStyleSheet(ITEM_STYLE)

        # Процесс:
        why_name = QLabel("Процесс:", item)
        why_name.setObjectName("label_header")
        why_name.setGeometry(10, 10, 60, 30)

        name_label = QLabel(process_name, item)
        name_label.setObjectName("label_value")
        name_label.setGeometry(75, 10, 200, 30)

        # Общее время:
        why_time = QLabel("Общее время:", item)
        why_time.setObjectName("label_header")
        why_time.setGeometry(285, 10, 90, 30)

        time_label = QLabel(time_text, item)
        time_label.setObjectName("time_value")
        time_label.setGeometry(380, 10, 150, 30)

        font = QFont()
        font.setPointSize(13)
        font.setWeight(QFont.Medium)
        time_label.setFont(font)

        # Кнопка:
        info_btn = QPushButton("Подробнее", item)
        info_btn.setProperty("process_name", process_name)
        info_btn.setGeometry(540, 10, 100, 30)

        def detail_info():
            id_session = self.comboBox.currentData()
            detail_window = DetailActivityDialog(id_session, info_btn.property("process_name"))
            detail_window.exec()

        info_btn.clicked.connect(detail_info)

        return item

    def add_item(self, process_name: str, time_text: str):
        index = self.layout.indexOf(self.spacer)
        item = self.create_item(process_name, time_text)
        self.layout.insertWidget(index, item)

    def add_combobox_item(self, name, userData):
        self.comboBox.addItem(name, userData)

    def clear_layout(self, layout):
        while layout.count():  # пока есть элементы
            item = layout.itemAt(0)
            if item.spacerItem():
                break
            widget = item.widget()  # если это виджет
            if widget is not None:
                widget.setParent(None)  # отключаем виджет от родителя
                widget.deleteLater()  # удаляем виджет из памяти