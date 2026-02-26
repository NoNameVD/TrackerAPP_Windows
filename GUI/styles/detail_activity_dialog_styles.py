DETAIL_ACTIVITY_DIALOG_STYLE = '''
            #DetailActivity {
                background-color: #1e1e1e;
            }
            
            /* Стили для QScrollArea */
            QScrollArea {
                background-color: transparent;
                border: none;
            }
            
            /* Стили для скроллбара */
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
            
            /* Стили для контейнера */
            QWidget#scrollContents {
                background-color: transparent;
                border: none;
            }
        '''

ACTIVITY_ITEM_STYLE = """
            #ActivityItem {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
            }
            
            #ActivityItem:hover {
                background-color: #333333;
                border: 1px solid #4a4a4a;
            }
            
            QLabel {
                color: #e0e0e0;
                background-color: transparent;
                border: none;
                font-size: 11px;
            }
            
            QLabel#label_header {
                color: #a0a0a0;
                font-size: 12px;
                font-weight: 600;
            }
            
            QLabel#label_value {
                color: #ffffff;
                font-size: 11px;
                background-color: #252525;
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                padding: 4px 6px;
            }
            
            QLabel#duration_label {
                color: #4a9eff;
                font-weight: 600;
                font-size: 12px;
                background-color: transparent;
            }
            
            QLabel#name_label {
                color: #ffffff;
                font-weight: 500;
                font-size: 11px;
                background-color: #252525;
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                padding: 4px 6px;
            }
        """
