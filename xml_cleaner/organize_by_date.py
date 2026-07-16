from pathlib import Path
import shutil

from xml_utils import abrir_xml
from xml_utils import obter_ano_mes


def organizar_por_data(xmls):

    for arquivo in xmls:

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