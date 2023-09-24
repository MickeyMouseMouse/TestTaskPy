from PyQt6.QtCore import QObject, pyqtSignal
from pathlib import Path
import re
from datetime import datetime
import random
import time


class Model(QObject):
    processing_started = pyqtSignal(int)
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, working_dir, file_type):
        super().__init__()
        self.working_dir = working_dir
        self.file_type = file_type

    def run(self):
        targets = []
        for child in self.working_dir.iterdir():
            if re.match(f".*_{self.file_type}.txt$", child.name):
                targets.append(child)

        amount = len(targets)
        if amount:
            self.processing_started.emit(amount)
            for i in range(amount):
                path = Path(targets[i].stem + f"_new_{datetime.now().strftime('%d.%m.%y_%H.%M')}.txt")
                with open(self.working_dir / path, "w") as f:
                    f.write(f"{random.randint(1, 1000)} {self.file_type}")
                time.sleep(0.7)
                self.progress.emit(i + 1)

        self.finished.emit()
