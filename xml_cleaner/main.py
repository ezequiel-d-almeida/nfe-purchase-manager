from pathlib import Path

from select_folder import selecionar_pasta
from remove_duplicates import remover_duplicados
from organize_by_date import organizar_por_data

OUTPUT_FOLDER = Path(__file__).parent / "output"


def main() -> Path:

    pasta_origem = selecionar_pasta()

    print("Removendo arquivos duplicados...")

    OUTPUT_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    xml_files = remover_duplicados(
        origem=pasta_origem,
        destino=OUTPUT_FOLDER
    )

    print("Organizando XMLs...")

    organizar_por_data(xml_files)

    print(f"XMLs processados: {len(xml_files)}")

    return OUTPUT_FOLDER


if __name__ == "__main__":
    main()