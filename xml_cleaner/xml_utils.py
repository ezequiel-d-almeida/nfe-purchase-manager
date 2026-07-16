from pathlib import Path
import xml.etree.ElementTree as ET


NAMESPACE = {
    "nfe": "http://www.portalfiscal.inf.br/nfe"
}


def abrir_xml(xml: Path):

    tree = ET.parse(xml)

    return tree.getroot()


def obter_chave(root):

    inf = root.find(".//nfe:infNFe", NAMESPACE)

    if inf is None:
        return None

    return inf.attrib["Id"][3:]


def obter_data(root):

    data = root.find(".//nfe:dhEmi", NAMESPACE)

    if data is None:
        data = root.find(".//nfe:dEmi", NAMESPACE)

    if data is None:
        return None

    return data.text


def obter_ano_mes(root):

    data = obter_data(root)

    if data is None:
        return None, None

    return data[:4], data[5:7]