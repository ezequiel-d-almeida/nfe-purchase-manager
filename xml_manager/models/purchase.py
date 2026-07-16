from dataclasses import dataclass, field

from models.product import Product


@dataclass
class Installment:

    numero: str

    vencimento: str

    valor: float


@dataclass
class Purchase:

    fornecedor: str

    cnpj: str

    numero_nf: str

    data_emissao: str

    valor_total: float

    parcelas: list[Installment] = field(default_factory=list)

    produtos: list[Product] = field(default_factory=list)