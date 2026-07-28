import xml.etree.ElementTree as ET
from datetime import datetime

from models.purchase import Purchase
from models.purchase import Installment
from models.product import Product
from pathlib import Path


NAMESPACE = {
    "nfe": "http://www.portalfiscal.inf.br/nfe"
}

class XMLReader:

    def read_xmls(
        self, 
        xml_files: list[Path]
    ) -> list[Purchase]:

        compras = []

        for arquivo in xml_files:

            try:

                compra = self._read_xml(arquivo)

                compras.append(compra)

            except Exception as e:

                print(f"Erro ao ler {arquivo.name}: {e}")

        return compras

    def _read_xml(self, arquivo):

        tree = ET.parse(arquivo)

        root = tree.getroot()

        fornecedor = self._text(root, ".//nfe:emit/nfe:xNome")

        cnpj = self._text(root, ".//nfe:emit/nfe:CNPJ")

        numero_nf = self._text(root, ".//nfe:ide/nfe:nNF")

        data_emissao = self._obter_data_emissao(root)

        valor_total_texto = self._text(root, ".//nfe:ICMSTot/nfe:vNF")

        valor_total = float(valor_total_texto) if valor_total_texto else 0.0

        compra = Purchase(
            fornecedor=fornecedor,
            cnpj=cnpj,
            numero_nf=numero_nf,
            data_emissao=data_emissao,
            valor_total=valor_total
        )

        compra.parcelas = self._read_installments(root)

        compra.produtos = self._read_products(root)

        return compra

    def _obter_data_emissao(self, root):

        data = self._text(root, ".//nfe:ide/nfe:dhEmi")

        if not data:
            data = self._text(root, ".//nfe:ide/nfe:dEmi")

        if not data:
            return None

        return datetime.strptime(data[:10], "%Y-%m-%d").date()

    def _read_installments(self, root):

        installments = []

        for dup in root.findall(".//nfe:dup", NAMESPACE):

            numero = self._text(dup, "nfe:nDup")
            vencimento_texto = self._text(dup, "nfe:dVenc")
            valor_texto = self._text(dup, "nfe:vDup")

            if not numero or not vencimento_texto or not valor_texto:
                continue

            parcela = Installment(
                numero=numero,
                vencimento=datetime.strptime(vencimento_texto[:10], "%Y-%m-%d").date(),
                valor=float(valor_texto)
            )

            installments.append(parcela)

        return installments

    def _read_products(self, root):

        produtos = []

        for det in root.findall(".//nfe:det", NAMESPACE):

            prod = det.find("nfe:prod", NAMESPACE)

            if prod is None:
                continue

            quantidade_texto = self._text(prod, "nfe:qCom")
            valor_unitario_texto = self._text(prod, "nfe:vUnCom")
            valor_total_texto = self._text(prod, "nfe:vProd")

            if not quantidade_texto or not valor_unitario_texto or not valor_total_texto:
                continue

            produto = Product(
                codigo=self._text(prod, "nfe:cProd"),
                descricao=self._text(prod, "nfe:xProd"),
                quantidade=float(quantidade_texto),
                unidade=self._text(prod, "nfe:uCom"),
                valor_unitario=float(valor_unitario_texto),
                valor_total=float(valor_total_texto)
            )

            produtos.append(produto)

        return produtos
    
    def _text(
        self,
        parent: ET.Element, 
        path: str
    ) -> str:

        element = parent.find(path, NAMESPACE)

        return element.text if element is not None else ""