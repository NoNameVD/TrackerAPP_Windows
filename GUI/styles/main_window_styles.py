MAIN_WINDOW_STYLE = """
            #MainWindow {
                background-color: #1e1e1e;
            }
            
            /* Стили для всех QLabel */
            QLabel {
                color: #e0e0e0;
                background-color: transparent;
                border: none;
                font-size: 13px;
            }
            
            /* Стили для QToolButton */
            QToolButton {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
                padding: 5px;
            }
            
            QToolButton:hover {
                background-color: #3d3d3d;
                border: 1px solid #4a9eff;
            }
            
            QToolButton:pressed {
                background-color: #252525;
                border: 1px solid #4a9eff;
            }
            
            /* Стили для QPushButton */
            QPushButton {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
            }
            
            QPushButton:hover {
                background-color: #5db0ff;
            }
            
            QPushButton:pressed {
                background-color: #3a8eef;
            }
            
            QPushButton:disabled {
                background-color: #3d3d3d;
                color: #6d6d6d;
            }
        """

STATE_TRACKER_STYLE_ACTIVE = """
            QLabel {
                color: #4a9eff;
                font-size: 12px;
                font-weight: 500;
                background-color: transparent;
            }
        """

STATE_TRACKER_STYLE_INACTIVE = """
                QLabel {
                    color: #ff6b6b;
                    font-size: 12px;
                    font-weight: 500;
                }
            """

MAIN_WIDGET_STYLE = """
            #main_widget {
                background-color: #1e1e1e;
                border: 1px solid #3d3d3d;
                border-radius: 10px;
            }
        """

COMBOBOX_STYLE = """
            QComboBox {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
                padding-left: 12px;
                padding-right: 30px;
                font-size: 13px;
                color: #e0e0e0;
                min-height: 38px;
            }
            
            QComboBox:hover {
                border: 1px solid #4a9eff;
                background-color: #333333;
            }
            
            QComboBox:focus {
                border: 1px solid #4a9eff;
                background-color: #2d2d2d;
            }
            
            QComboBox::drop-down {
                border: none;
                width: 30px;
                background-color: transparent;
            }
            
            QComboBox::down-arrow {
                image: none;
                border-left: 10px solid transparent;
                border-right: 10px solid transparent;
                border-top: 11px solid #a0a0a0;
                margin-right: 8px;
            }
            
            QComboBox::down-arrow:hover {
                border-top: 15px solid #4a9eff;
            }
            
            QComboBox QAbstractItemView {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 6px;
                selection-background-color: #4a9eff;
                selection-color: #ffffff;
                color: #e0e0e0;
                padding: 4px;
                outline: none;
            }
            
            QComboBox QAbstractItemView::item {
                padding: 4px 12px;
                border-radius: 4px;
                min-height: 20px;
            }
            
            QComboBox QAbstractItemView::item:hover {
                background-color: #3d3d3d;
            }
            
            QComboBox QAbstractItemView::item:selected {
                background-color: #4a9eff;
                color: #ffffff;
            }
        """

UPDATE_BUTTON_STYLE = """
            QToolButton {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
                padding: 5px;
            }
            
            QToolButton:hover {
                background-color: #3d3d3d;
                border: 1px solid #4a9eff;
            }
            
            QToolButton:pressed {
                background-color: #252525;
            }
        """

SCROLL_AREA_STYLE = """
            QScrollArea {
                background-color: transparent;
                border: none;
            }
            
            QScrollBar:vertical {
                background-color: #1e1e1e;
                width: 12px;
                border-radius: 6px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background-color: #3d3d3d;
                border-radius: 6px;
                min-height: 30px;
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: #4a9eff;
            }
            
            QScrollBar::handle:vertical:pressed {
                background-color: #3a8eef;
            }
            
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }
        """

SCROLL_CONTENTS_STYLE = """ 
            QWidget {
                background-color: transparent;
                border: none;
            }
         """

ITEM_STYLE = """
            #Item {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
            }
            
            #Item:hover {
                background-color: #333333;
                border: 1px solid #4a4a4a;
            }
            
            QLabel {
                color: #e0e0e0;
                background-color: transparent;
                border: none;
                font-size: 12px;
            }
            
            QLabel#label_header {
                color: #a0a0a0;
                font-size: 11px;
                font-weight: 500;
            }
            
            QLabel#label_value {
                color: #ffffff;
                font-size: 12px;
                background-color: #252525;
                border: 1px solid #3d3d3d;
                border-radius: 6px;
                padding: 5px 8px;
            }
            
            QLabel#time_value {
                color: #4a9eff;
                font-size: 13px;
                font-weight: 600;
                background-color: #252525;
                border: 1px solid #3d3d3d;
                border-radius: 6px;
                padding: 5px 8px;
            }
            
            QPushButton {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: 500;
            }
            
            QPushButton:hover {
                background-color: #5db0ff;
            }
            
            QPushButton:pressed {
                background-color: #3a8eef;
            }
        """

BASE_INFO_STYLES = """
    QWidget {
        background-color: #2d2d2d;
        border: 1px solid #3d3d3d;
        border-radius: 10px;
        padding: 8px;
    }

    /* Номер сессии (заголовок) */
    QLabel#session_number {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #4a9eff, stop:1 #3a8eef);
        color: #ffffff;
        border: none;
        border-radius: 8px;
        font-size: 15px;
        font-weight: 700;
        padding: 10px 12px;
        margin-right: 20px;
        max-width: 80px;
    }

    /* Заголовки полей (Время начала:, и т.д.) */
    QLabel#label_header {
        color: #a0a0a0;
        background-color: transparent;
        border: none;
        font-size: 12px;
        font-weight: 600;
        padding: 2px 4px;
        margin-right: 4px;
    }

    /* Значения полей */
    QLabel#label_value {
        color: #ffffff;
        background-color: #1e1e1e;
        border: 1px solid #3d3d3d;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 500;
        padding: 8px 12px;
        margin-right: 15px;
        min-width: 80px;
    }
"""