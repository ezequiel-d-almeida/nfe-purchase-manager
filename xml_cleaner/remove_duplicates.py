from pathlib import Path
import shutil

from xml_utils import abrir_xml
from xml_utils import obter_chave


def remover_duplicados(origem: Path, destino: Path):

    destino.mkdir(
        parents=True,
        exist_ok=True
    )

    chaves = set()

    xmls = []

    # Carrega as chaves de notas já organizadas em execuções anteriores,
    # para não copiar de novo o que já está em destino/AAAA/MM/
    for arquivo in destino.rglob("*.xml"):

        try:

            root = abrir_xml(arquivo)

            chave = obter_chave(root)

            if chave is not None:
                chaves.add(chave)

        except Exception:
            continue

    for arquivo in origem.glob("*.xml"):

        try:

            root = abrir_xml(arquivo)

            chave = obter_chave(root)

            if chave is None:
                continue

            if chave in chaves:
                continue

            chaves.add(chave)

            novo = destino / arquivo.name

            shutil.copy2(arquivo, novo)

            xmls.append(novo)

        except Exception as e:

            print(f"Erro ao processar {arquivo.name}: {e}")

            continue

    return xmls