import csv
import os.path
from pathlib import Path

import logger


class Store:
    file_name: str
    logger = logger.get_logger(__name__)

    def __init__(self, file_name):
        self.file_name = file_name
        try:
            f = open(self.file_name)
            self.logger.info(f"Файл {self.file_name} открывается")
        except IOError:
            f = open(self.file_name, 'w')
            self.logger.info(f"Файла {self.file_name} нет, создание")
        f.close()

    def read_all(self):
        all_rows = []
        with open(self.file_name, 'r') as file:
            csvreader = csv.reader(file, delimiter=';')
            for row in csvreader:
                all_rows.append(row)
        self.logger.info("Все заметки прочитаны")
        return all_rows

    def save_all(self, rows):
        p = Path(self.file_name)
        file_without_ext = p.stem
        backup_file = file_without_ext + '.bak'
        if os.path.exists(backup_file):
            os.remove(backup_file)
        os.rename(self.file_name, backup_file)
        with open(self.file_name, 'w') as file:
            csvwriter = csv.writer(file, delimiter=';')
            csvwriter.writerows(rows)
        self.logger.info("Все заметки сохранены")