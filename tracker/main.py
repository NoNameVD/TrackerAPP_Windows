import win32gui as ui
import win32process
import win32process as proc
import win32con
import win32api as api
import time
from datetime import datetime, timedelta
from db_using import start_session, update_session, update_activity

def get_app_info():
    current_focus_hwnd = ui.GetForegroundWindow() # Получение hwnd
    pid = proc.GetWindowThreadProcessId(current_focus_hwnd)[1] # Получение айди процесса

    try:
        process_handle = api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION, False, pid) # Ссылка на процесс
    except Exception:
        return None

    exe_path = win32process.GetModuleFileNameEx(process_handle, None) # Путь к исполняемому файлу
    exe_split = exe_path.split('\\')

    name_process = exe_split[len(exe_split)-1] # Имя процесса
    return name_process

def main():
    start_time = ""
    active_app = None
    last_time = datetime.now()
    INTERVAL = timedelta(seconds=30)

    id_session = start_session()

    while True:
        name = get_app_info()
        if name is None:
            continue

        current_time = datetime.now()

        if current_time - last_time >= INTERVAL:
            last_time = current_time
            update_session(id_session)

        if active_app is None:
            active_app = name
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time.sleep(1)
            continue

        if name != active_app:
            end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            update_activity(id_session, active_app, start_time, end_time)

            active_app = name
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)

if __name__ == '__main__':
    main()


