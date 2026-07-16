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

    return list(folder.rglob("*.xml"))

def main(xml_folder: Path | None = None):

    if xml_folder is None:
        xml_folder = select_xml_folder()

    xml_files = get_xml_files(xml_folder)

    if not xml_files:

        print("Nenhum XML encontrado.")

        return

    print(f"{len(xml_files)} XML(s) encontrado(s).")

    reader = XMLReader()

    purchases = reader.read_xmls(xml_files)

    writer = ExcelWriter()

    output_file = xml_folder / "Compras.xlsx"

    writer.write(purchases, output_file)

    Report.generate(purchases)

    try:

        os.startfile(output_file)

    except AttributeError:

        pass

    except Exception:

        pass

    print(f"\nArquivo salvo em:\n{output_file}")

if __name__ == "__main__":
     main()