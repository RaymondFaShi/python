import subprocess
import sys


def main():
    subprocess.run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--clean",
            "--onefile",
            "--windowed",
            "--name",
            "Calculator",
            "app/main.py",
        ],
        check = True,
    )


if __name__ == "__main__":
    main()