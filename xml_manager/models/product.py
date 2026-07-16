from dataclasses import dataclass


@dataclass
class Product:

    codigo: str

    descricao: str

    quantidade: float

    unidade: str

    valor_unitario: float

    valor_total: float