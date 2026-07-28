from pathlib import Path
import xml.etree.ElementTree as ET


NFE_NAMESPACE = {
    "nfe": "http://www.portalfiscal.inf.br/nfe"
}


def abrir_xml(xml: Path) -> ET.Element:

    tree = ET.parse(xml)

    return tree.getroot()


def obter_chave(root) -> str | None:

    inf = root.find(".//nfe:infNFe", NFE_NAMESPACE)

    if inf is None:
        return None

    invoice_id = inf.attrib["Id"]

    return invoice_id.removeprefix("NFe")


def obter_data(root) -> str | None:

    issue_data = root.find(".//nfe:dhEmi", NFE_NAMESPACE)

    if issue_data is None:
        issue_data = root.find(".//nfe:dEmi", NFE_NAMESPACE)

    if issue_data is None:
        return None

    return issue_data.text


def obter_ano_mes(root) -> tuple[str | None, str | None]:

    data = obter_data(root)

    if data is None:
        return None, None

    year = data[:4]
    month = data[5:7]

    return year, month