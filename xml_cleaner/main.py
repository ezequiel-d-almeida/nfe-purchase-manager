from pathlib import Path

from select_folder import selecionar_pasta
from remove_duplicates import remover_duplicados
from organize_by_date import organizar_por_data


OUTPUT_FOLDER = Path("output")


def main():

    pasta = selecionar_pasta()

    print("Removendo arquivos duplicados...")

    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    xmls = remover_duplicados(
        origem=pasta,
        destino=OUTPUT_FOLDER
    )

    print("Organizando XMLs...")

    organizar_por_data(xmls)

    print()

    print("Processo finalizado.")
    print(f"XMLs processados: {len(xmls)}")

    return OUTPUT_FOLDER


if __name__ == "__main__":
    main()