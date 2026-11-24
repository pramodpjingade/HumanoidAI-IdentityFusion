
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
VOICE_SCRIPT = BASE_DIR / "voice_recognition" / "recognize_voice_clean.py"


def recognize_voice():
    result = subprocess.run(
        [sys.executable, str(VOICE_SCRIPT)],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        return None

    for line in result.stdout.splitlines():
        if line.startswith("Recognized speaker:"):
            return line.split(":", 1)[1].strip()

        if "Unknown speaker detected!" in line:
            return None

    return None


if __name__ == "__main__":
    identity = recognize_voice()
    print("\nVoice adapter result:", identity)
