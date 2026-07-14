from models.purchase import Purchase


class Report:

    @staticmethod
    def generate(purchases: list[Purchase]):

        total_notas = len(purchases)

        total_fornecedores = len(
            set(p.fornecedor for p in purchases)
        )

        total_produtos = sum(
            len(p.produtos)
            for p in purchases
        )

        total_parcelas = sum(
            len(p.parcelas)
            for p in purchases
        )

        valor_total = sum(
            p.valor_total
            for p in purchases
        )

        print("\n" + "=" * 60)
        print("RELATÓRIO DO PROCESSAMENTO")
        print("=" * 60)

        print(f"Notas processadas : {total_notas}")
        print(f"Fornecedores      : {total_fornecedores}")
        print(f"Produtos          : {total_produtos}")
        print(f"Parcelas          : {total_parcelas}")
        print(f"Valor Total       : R$ {valor_total:,.2f}")

        print("=" * 60)