from pathlib import Path
import shutil

from xml_cleaner.nfe_parser import abrir_xml
from xml_cleaner.nfe_parser import obter_chave

def remover_duplicados(
        origem: Path,
        destino: Path
    ) -> list[Path]:

    destino.mkdir(
        parents=True,
        exist_ok=True
    )

    processed_keys = set()

    new_xml_files = []

    # Carrega as chaves das NF-es já processadas para garantir que execuções futuras não importem documentos duplicados.
    for arquivo in destino.rglob("*.xml"):

        try:

            root = abrir_xml(arquivo)

            invoice_key = obter_chave(root)

            if invoice_key is not None:
                processed_keys.add(invoice_key)

        except Exception:
            continue

    for arquivo in origem.glob("*.xml"):

        try:

            root = abrir_xml(arquivo)

            invoice_key = obter_chave(root)

            if invoice_key is None:
                continue

            if invoice_key in processed_keys:
                continue

            processed_keys.add(invoice_key)

            novo = destino / arquivo.name

            shutil.copy2(arquivo, novo)

            new_xml_files.append(novo)

        except Exception as e:

            print(f"Erro ao processar {arquivo.name}: {e}")

            continue

    return new_xml_files