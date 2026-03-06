#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> text = "23 + 42 * 10"
>>> parse(text)
foo
"""

from __future__ import annotations


class Node:
    def __init__(
        self, val: float | str, left: Node | None = None, right: Node | None = None
    ):
        self._val = val
        self._left = left
        self._right = right


class BinaryOperator(Node):
    def __init__(self, **kwargs):
        super().__init__(self.operator, **kwargs)


class Plus(BinaryOperator):
    operator = "+"


class Minus(BinaryOperator):
    operator = "-"


class Mul(BinaryOperator):
    operator = "*"


class Div(BinaryOperator):
    operator = "/"


class UnaryOperator(Node):
    def __init__(self, val):
        super().__init__(val)


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, val):
        super().__init__(val)


def parse(text_: str) -> Node:
    return Plus(left=Number(23), right=Mul(left=Number(42), right=Number(10)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
