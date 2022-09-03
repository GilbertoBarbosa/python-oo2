# ABC - abstract base classes
from abc import ABC

from collections.abc import MutableSequence
from numbers import Complex


class Numero(MutableSequence):
    def __getitem__(self, item):
        super().__getitem__()



filmes = Numero()


