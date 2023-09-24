import sys
from pathlib import Path
import re
from datetime import datetime
import random


class Model:
    def __init__(self, working_dir=Path(), file_type=""):
        self.working_dir = working_dir
        self.file_type = file_type

    def setWorkingDir(self, working_dir: Path):
        self.working_dir = working_dir

    def setFileType(self, file_type: str):
        self.file_type = file_type

    def handle(self):
        for child in self.working_dir.iterdir():
            if not re.match(f".*_{self.file_type}.txt$", child.name):
                continue
            path = Path(child.stem + f"_new_{datetime.now().strftime('%d.%m.%y_%H.%M')}.txt")
            with open(self.working_dir / path, "w") as f:
                f.write(f"{random.randint(1, 1000)} {self.file_type}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        Model(Path(sys.argv[1]), sys.argv[2]).handle()
