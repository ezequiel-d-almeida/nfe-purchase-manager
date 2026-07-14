from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import os
from extractor.xml_reader import XMLReader
from output.excel_writer import ExcelWriter
from utils.report import Report


def select_xml_folder():

    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory(
        title="Selecione a pasta que contém os XMLs"
    )

    if not folder:
        print("Nenhuma pasta foi selecionada.")
        exit()

    return Path(folder)


def get_xml_files(folder: Path):

    return list(folder.glob("*.xml"))


def main():

    xml_folder = select_xml_folder()

    arquivos = get_xml_files(xml_folder)

    if not arquivos:
        print("Nenhum XML encontrado.")
        return

    print(f"{len(arquivos)} arquivo(s) encontrado(s).")

    reader = XMLReader()

    compras = reader.read_xmls(arquivos)

    writer = ExcelWriter()

    output_file = xml_folder / "Compras.xlsx"

    writer.write(compras, output_file)

    try:

        os.startfile(output_file)

    except Exception as e:

        print(f"Não foi possível abrir o arquivo automaticamente: {e}")

    Report.generate(compras)

    print(f"\nArquivo salvo em:\n{output_file}")


if __name__ == "__main__":

    main()