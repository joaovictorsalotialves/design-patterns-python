"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""
from typing import Any, List
from collections.abc import Iterator, Iterable


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def next(self) -> Any:
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def next(self) -> Any:
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._itens: List[Any] = []
        self._my_iterator = MyIterator(self._itens)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._itens)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._itens})'

    def add(self, value: Any) -> None:
        self._itens.append(value)


if __name__ == '__main__':
    mylist = MyList()
    mylist.add('João')
    mylist.add('Vinicius')
    mylist.add('Davi')

    # print(mylist)

    # print('ROUBEI O VALOR: ', next(mylist.__iter__()))

    for value in mylist:
        print(value)

    print()

    for value in mylist.reverse_iterator():
        print(value)
