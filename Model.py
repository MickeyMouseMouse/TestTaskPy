from PyQt6.QtCore import QObject, pyqtSignal
from pathlib import Path
import re
from datetime import datetime
import random
import time


class Model(QObject):
    started = pyqtSignal(int)  # reports the number of processing files
    progress = pyqtSignal(int)  # reports the number of files already processed
    finished = pyqtSignal()

    def __init__(self, working_dir, file_type):
        super().__init__()
        self.working_dir = working_dir
        self.file_type = file_type

    def run(self):
        targets = set()
        for child in self.working_dir.iterdir():  # search for desired files
            if re.match(f".*_{self.file_type}.txt$", child.name):
                targets.add(child.name)

        for child in self.working_dir.iterdir():  # exclude already processed files
            m = re.match("(?P<name>.*)(_new_)(.)*(\\.txt)$", child.name)
            if m:
                old_file_name = f"{m.group('name')}.txt"
                if old_file_name in targets:
                    targets.discard(old_file_name)

        self.started.emit(len(targets))
        num = 0
        for target in targets:
            path = Path(target[:-4] + f"_new_{datetime.now().strftime('%d.%m.%y_%H.%M')}.txt")
            with open(self.working_dir / path, "w") as f:
                f.write(f"{random.randint(1, 1000)} {self.file_type}")

            time.sleep(0.5)  # artificial delay

            num += 1
            self.progress.emit(num)

        self.finished.emit()
