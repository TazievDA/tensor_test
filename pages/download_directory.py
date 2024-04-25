import os
from pathlib import Path

class DownloadDirectory:

    @staticmethod
    def check_file_presence():
        root_path = Path(__file__).resolve().parents[1]
        if 'sbisplugin-setup-web.exe' in os.listdir(root_path):
            return 'OK'
        else:
            return 'Файл не загружен.'
    @staticmethod
    def check_file_size():
        root_path = Path(__file__).resolve().parents[1]
        file_size = os.path.getsize(f'{root_path}\\sbisplugin-setup-web.exe')
        file_size_in_mb = f"{round(file_size / 1048576, 2)} МБ"
        return file_size_in_mb