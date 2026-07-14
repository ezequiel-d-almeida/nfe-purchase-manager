import logging
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

from models.product import Product
from models.purchase import Purchase, Installment


NAMESPACE = {
    "nfe": "http://www.portalfiscal.inf.br/nfe"
}

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class XMLReader:

    def read_xmls(self, xml_files: list[Path]) -> list[Purchase]:

        purchases = []

        total = len(xml_files)

        logger.info(f"Iniciando processamento de {total} XML(s)...")

        for file in xml_files:

            try:

                purchase = self.read_xml(file)

                purchases.append(purchase)

                logger.info(f"OK -> {file.name}")

            except Exception as e:

                logger.error(f"ERRO -> {file.name}")
                logger.exception(e)

        logger.info(f"{len(purchases)} XML(s) processado(s) com sucesso.")

        return purchases

    def read_xml(self, file_path: Path) -> Purchase:

        tree = ET.parse(file_path)

        root = tree.getroot()

        fornecedor = self._get_supplier(root)

        cnpj = self._get_supplier_cnpj(root)

        numero_nf = self._get_invoice_number(root)

        data = self._get_issue_date(root)

        valor = self._get_total_value(root)

        parcelas = self._get_installments(root)

        produtos = self._get_products(root)

        return Purchase(
            fornecedor=fornecedor,
            cnpj=cnpj,
            numero_nf=numero_nf,
            data_emissao=data,
            valor_total=valor,
            parcelas=parcelas,
            produtos=produtos
        )

    def _get_supplier(self, root):

        return self._get_text(
            root,
            ".//nfe:emit/nfe:xNome"
        )

    def _get_supplier_cnpj(self, root):

        return self._get_text(
            root,
            ".//nfe:emit/nfe:CNPJ"
        )

    def _get_invoice_number(self, root):

        return self._get_text(
            root,
            ".//nfe:ide/nfe:nNF"
        )

    def _get_issue_date(self, root):

        data = self._get_text(
            root,
            ".//nfe:ide/nfe:dhEmi"
        )

        if not data:
            return ""

        return datetime.fromisoformat(data).strftime("%d/%m/%Y")

    def _get_total_value(self, root):

        valor = self._get_text(
            root,
            ".//nfe:ICMSTot/nfe:vNF"
        )

        return float(valor) if valor else 0.0

    def _get_installments(self, root):

        installments = []

        duplicatas = root.findall(
            ".//nfe:dup",
            NAMESPACE
        )

        for dup in duplicatas:

            numero = self._get_text(
                dup,
                "nfe:nDup"
            )

            vencimento = self._get_text(
                dup,
                "nfe:dVenc"
            )

            valor = self._get_text(
                dup,
                "nfe:vDup"
            )

            installments.append(

                Installment(
                    numero=numero,
                    vencimento=vencimento,
                    valor=float(valor) if valor else 0.0
                )

            )

        return installments

    def _get_products(self, root):

        products = []

        itens = root.findall(
            ".//nfe:det",
            NAMESPACE
        )

        for item in itens:

            produto = item.find(
                "nfe:prod",
                NAMESPACE
            )

            if produto is None:
                continue

            quantidade = self._get_text(
                produto,
                "nfe:qCom"
            )

            valor_unitario = self._get_text(
                produto,
                "nfe:vUnCom"
            )

            valor_total = self._get_text(
                produto,
                "nfe:vProd"
            )

            products.append(

                Product(
                    codigo=self._get_text(
                        produto,
                        "nfe:cProd"
                    ),

                    descricao=self._get_text(
                        produto,
                        "nfe:xProd"
                    ),

                    quantidade=float(quantidade) if quantidade else 0.0,

                    unidade=self._get_text(
                        produto,
                        "nfe:uCom"
                    ),

                    valor_unitario=float(valor_unitario) if valor_unitario else 0.0,

                    valor_total=float(valor_total) if valor_total else 0.0
                )

            )

        return products

    def _get_text(self, parent, tag):

        element = parent.find(
            tag,
            NAMESPACE
        )

        if element is None:
            return ""

        return element.text or ""