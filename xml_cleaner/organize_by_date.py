from pathlib import Path
import shutil

from xml_cleaner.nfe_parser import abrir_xml
from xml_cleaner.nfe_parser import obter_ano_mes


def organizar_por_data(
        xml_files: list[Path]
) -> None:

    for arquivo in xml_files:

        root = abrir_xml(arquivo)

        ano, mes = obter_ano_mes(root)

        if ano is None:
            continue

        destino = arquivo.parent / ano / mes

        destino.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.move(
            arquivo,
            destino / arquivo.name
        )