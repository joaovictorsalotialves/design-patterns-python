"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class A(StringReprMixin):
    def __init__(self, nome) -> None:
        self.x = 10
        self.y = 20
        self.nome = nome


class MonoStateSimple(StringReprMixin):
    _state: dict = {
        'x': 10,
        'y': 20,
    }

    def __init__(self, nome=None, sobrenome=None) -> None:
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == '__main__':
    m1 = MonoStateSimple(nome='João Victor')
    m2 = MonoStateSimple(sobrenome='Saloti Alves')
    print(m1)
    print(m2)
