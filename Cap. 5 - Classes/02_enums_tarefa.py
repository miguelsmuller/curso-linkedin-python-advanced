# define enumerations using the Enum base class
from enum import Enum, auto

# TODO: Defina a classe Fruta que herda de Enum
class Fruta(Enum):
    UVA = 1
    BABANA = 2
    LARANJA = 3
    TOMATE = 4
    PERA = auto()

def main():
    # TODO: Objetos enum possuem valores e tipos de fácil leitura
    print(Fruta.UVA)
    print(type(Fruta.UVA))
    print(repr(Fruta.UVA))

    # TODO: Objetos enum possuem propriedades "name" (nome) e
    # "value" (valor)
    print(Fruta.UVA.name, Fruta.UVA.value)

    # TODO: Mostre o valor gerado automaticamente para PERA)
    print(Fruta.PERA.value)

    # TODO: É possível usar objetos enum como chaves
    frutas = dict()
    frutas[Fruta.BABANA] = "Casca Amarela"
    print(frutas[Fruta.BABANA])


if __name__ == "__main__":
    main()
