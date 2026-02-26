HI_WINDOW_STYLE = '''
            #hi_window {
                background-color: #1e1e1e;
            }
            
            /* Стили для QLabel */
            QLabel {
                font-size: 14px;
                color: #e0e0e0;
                background-color: transparent;
                line-height: 1.6;
            }
            
            QLabel#label_info {
                color: #a0a0a0;
                font-size: 13px;
            }
            
            /* Стили для QCheckBox */
            QCheckBox {
                color: #e0e0e0;
                font-size: 12px;
                spacing: 8px;
                background-color: transparent;
            }
            
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #3d3d3d;
                border-radius: 5px;
                background-color: #2d2d2d;
            }
            
            QCheckBox::indicator:hover {
                border: 2px solid #4a9eff;
                background-color: #333333;
            }
            
            QCheckBox::indicator:checked {
                background-color: #4a9eff;
                border: 2px solid #4a9eff;
            }
            
            QCheckBox::indicator:checked:hover {
                background-color: #5db0ff;
                border: 2px solid #5db0ff;
            }
            
            /* Стили для QPushButton */
            QPushButton {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
            }
            
            QPushButton:hover {
                background-color: #3d3d3d;
                border: 1px solid #4a9eff;
                color: #ffffff;
            }
            
            QPushButton:pressed {
                background-color: #252525;
                border: 1px solid #4a9eff;
            }
            
            /* Акцентная кнопка OK */
            QPushButton#button_ok {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
                min-width: 18px;
                min-height: 18px;
            }
            
            QPushButton#button_ok:hover {
                background-color: #5db0ff;
            }
            
            QPushButton#button_ok:pressed {
                background-color: #3a8eef;
            }
            
            /* Кнопка настроек */
            QPushButton#button_settings {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
            }
            
            QPushButton#button_settings:hover {
                background-color: #5db0ff;
            }
            
            QPushButton#button_settings:pressed {
                background-color: #3a8eef;
            }
        '''
