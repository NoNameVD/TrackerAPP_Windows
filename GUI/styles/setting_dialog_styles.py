SETTINGS_DIALOG_STYLE = '''
            #Settings {
                background-color: #1e1e1e;
            }
            
            /* Стили для QCheckBox */
            QCheckBox {
                color: #e0e0e0;
                font-size: 13px;
                spacing: 8px;
                background-color: transparent;
            }
            
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #3d3d3d;
                border-radius: 6px;
                background-color: #2d2d2d;
            }
            
            QCheckBox::indicator:hover {
                border: 2px solid #4a9eff;
                background-color: #333333;
            }
            
            QCheckBox::indicator:checked {
                background-color: #4a9eff;
                border: 2px solid #4a9eff;
                image: none;
            }
            
            QCheckBox::indicator:checked:hover {
                background-color: #5db0ff;
                border: 2px solid #5db0ff;
            }
            
            /* Имитация галочки через градиент */
            QCheckBox::indicator:checked {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #4a9eff, stop:1 #3a8eef);
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
            
            /* Специальные стили для кнопок действий */
            QPushButton#btn_ok {
                background-color: #4a9eff;
                color: #ffffff;
                border: none;
            }
            
            QPushButton#btn_ok:hover {
                background-color: #5db0ff;
            }
            
            QPushButton#btn_ok:pressed {
                background-color: #3a8eef;
            }
            
            QPushButton#reset_app {
                background-color: #ff6b6b;
                color: #ffffff;
                border: none;
            }
            
            QPushButton#reset_app:hover {
                background-color: #ff8787;
            }
            
            QPushButton#reset_app:pressed {
                background-color: #ee5a5a;
            }
            
            QPushButton#reset_db {
                background-color: #ffa94d;
                color: #ffffff;
                border: none;
            }
            
            QPushButton#reset_db:hover {
                background-color: #ffb866;
            }
            
            QPushButton#reset_db:pressed {
                background-color: #f09838;
            }
        '''
