import os

import gspread
from gspread.utils import ValueInputOption

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

from models.purchase import Purchase


class SheetsWriter:

    def __init__(self):

        load_dotenv()

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]

        credentials = Credentials.from_service_account_file(
            os.getenv("GOOGLE_CREDENTIALS"),
            scopes=scopes
        )

        client = gspread.authorize(credentials)

        self.spreadsheet = client.open_by_key(
            os.getenv("GOOGLE_SHEET_ID")
        )

    def write(self, purchases: list[Purchase]):

        self._write_purchase_sheet(purchases)

        self._write_installment_sheet(purchases)

        self._write_product_sheet(purchases)

        print("\nGoogle Sheets atualizado com sucesso!")

    def _get_or_create_sheet(self, title):

        try:

            sheet = self.spreadsheet.worksheet(title)

        except gspread.WorksheetNotFound:

            sheet = self.spreadsheet.add_worksheet(
                title=title,
                rows=100,
                cols=20
            )

        sheet.clear()

        return sheet

    def _write_purchase_sheet(self, purchases):

        sheet = self._get_or_create_sheet("Compras")

        rows = [[
            "Fornecedor",
            "CNPJ",
            "Número NF",
            "Data",
            "Valor Total",
            "Qtd Parcelas"
        ]]

        for purchase in purchases:

            rows.append([
                purchase.fornecedor,
                purchase.cnpj,
                purchase.numero_nf,
                purchase.data_emissao.isoformat() if purchase.data_emissao else "",
                purchase.valor_total,
                len(purchase.parcelas)
            ])

        sheet.update(rows, value_input_option=ValueInputOption.user_entered)

    def _write_installment_sheet(self, purchases):

        sheet = self._get_or_create_sheet("Parcelas")

        rows = [[
            "Número NF",
            "Fornecedor",
            "Parcela",
            "Vencimento",
            "Valor"
        ]]

        for purchase in purchases:

            for installment in purchase.parcelas:

                rows.append([
                    purchase.numero_nf,
                    purchase.fornecedor,
                    installment.numero,
                    installment.vencimento.isoformat(),
                    installment.valor
                ])

        sheet.update(rows, value_input_option=ValueInputOption.user_entered)

    def _write_product_sheet(self, purchases):

        sheet = self._get_or_create_sheet("Produtos")

        rows = [[
            "Número NF",
            "Fornecedor",
            "Código",
            "Produto",
            "Quantidade",
            "Unidade",
            "Valor Unitário",
            "Valor Total"
        ]]

        for purchase in purchases:

            for product in purchase.produtos:

                rows.append([
                    purchase.numero_nf,
                    purchase.fornecedor,
                    product.codigo,
                    product.descricao,
                    product.quantidade,
                    product.unidade,
                    product.valor_unitario,
                    product.valor_total
                ])

        sheet.update(rows)