from select_folder import selecionar_pasta
from remove_duplicates import remover_duplicados
from organize_by_date import organizar_por_data

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "xml_manager"))

from main import main as manager_main


OUTPUT_FOLDER = Path(__file__).parent / "output"


def main():

    pasta_origem = selecionar_pasta()

    print("Removendo arquivos duplicados...")

    OUTPUT_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    xmls = remover_duplicados(
        origem=pasta_origem,
        destino=OUTPUT_FOLDER
    )

    print("Organizando XMLs...")

    organizar_por_data(xmls)

    print(f"XMLs processados: {len(xmls)}")

    manager_main(OUTPUT_FOLDER)


if __name__ == "__main__":
    main()