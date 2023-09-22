import sys
from pathlib import Path
import re
from datetime import datetime
import random


def handle(working_dir, file_type):
	path = Path(working_dir)
	for child in path.iterdir():
		if not re.search(f"_{file_type}.txt", child.name):
			continue
		new_file = path / Path(child.stem + f"_new_{datetime.now().strftime('%d.%m.%y_%H.%M')}.txt")
		with open(new_file, "w") as f:
			f.write(f"{random.randint(1, 1000)} {file_type}")


if __name__ == "__main__":
	if len(sys.argv) == 3:
		handle(sys.argv[1], sys.argv[2])

