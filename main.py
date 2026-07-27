from pathlib import Path

from xml_cleaner.main import main as cleaner_main
from xml_manager.main import main as manager_main


def main():

    output_folder: Path = cleaner_main()

    if output_folder is None:
        return

    manager_main(output_folder)


if __name__ == "__main__":
    main()