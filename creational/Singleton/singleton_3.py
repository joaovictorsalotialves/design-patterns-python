# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('CALL é executado')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW é executado')
#         return super().__new__(cls)

#     def __init__(self, nome) -> None:
#         print('INIT é executado')
#         self.nome = nome


# p1 = Pessoa('João')

from typing import Dict


class Singleton(type):
    _instaces: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instaces:
            cls._instaces[cls] = super().__call__(*args, **kwargs)
        return cls._instaces[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        print('OI')
        self.tema = 'Tema Escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema Claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)
