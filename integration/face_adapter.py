
import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "datasets" / "recognition_log.csv"


def recognize_face(max_age_seconds=30):

    if not LOG_FILE.exists():
        return None

    with open(LOG_FILE, "r", newline="") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        return None

    latest = rows[-1]

    timestamp = datetime.strptime(
        latest["Date"] + " " + latest["Time"],
        "%Y-%m-%d %H:%M:%S"
    )

    age = (datetime.now() - timestamp).total_seconds()

    if age < 0 or age > max_age_seconds:
        return None

    name = latest["Person"].strip()

    if name.casefold() in {
        "", "unknown", "unknown person", "none"
    }:
        return None

    return name


if __name__ == "__main__":
    identity = recognize_face()
    print("Face adapter result:", identity)
