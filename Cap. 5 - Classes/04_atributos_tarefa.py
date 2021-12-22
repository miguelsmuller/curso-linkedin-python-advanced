# Personalizando a representação string de uma classe
from typing import Any


class MinhasCores():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: Use getattr para retornar um valor de forma dinâmica
    def __getattr__(self, __name):
        if __name== "rgb":
            return (self.red, self.green, self.blue)
        else:
            raise AttributeError

    # TODO: Use setattr para retornar um valor de forma dinâmica
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name== "rgb":
            self.red = __value[0]
            self.green = __value[1]
            self.blue = __value[2]
            return ()
        else:
            super().__setattr__(__name, __value)

    # TODO: Use dir para listar os atributos disponíveis
    def __dir__(self):
        return ("red", "green", "blue", "rgb")


def main():
    # Criando uma instância de MinhasCores
    cores = MinhasCores()

    # TODO: Mostre o valor de um atributo
    print(cores.rgb)

    # TODO: Defina o valor de um atributo
    cores.rgb = (125, 200, 83)
    print(cores.rgb)

    # TODO: Acesse um atributo específico
    print(cores.red)

    # TODO: Liste os atributos disponíveis
    print(dir(cores))

if __name__ == "__main__":
    main()
