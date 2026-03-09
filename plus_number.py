#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> text = "23 + 42 * 10"
>>> parse(input_str)
Plus(23, Mul(42, 10))
"""

from __future__ import annotations
from typing import Iterator
from run import tokens_iter, Token
from run import text as input_str  # noqa: F401


class Node:
    def __init__(
        self, val: float | str, left: Node | None = None, right: Node | None = None
    ):
        self._val = val
        self._left = left
        self._right = right

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}({self._val!r}, {self._left}, {self._right})"


class BinaryOperator(Node):
    def __init__(self, left, right):
        super().__init__(self.operator, left, right)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}({self._left}, {self._right})"


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

    def __repr__(self):
        return f"Number({self._val!r})"


def expr(tok_stream) -> Node:
    res = term(tok_stream)
    ops = {"PLUS": Plus, "MINUS": Minus}
    while (op := tok_stream.peek())._type in ops:
        tok_stream.next()
        res = ops[op._type](res, term(tok_stream))
    return res


def term(tok_stream) -> Node:
    res: Node = factor(tok_stream)
    ops = {"TIMES": Mul, "DIVIDE": Div}
    while (op := tok_stream.peek())._type in ops:
        tok_stream.next()
        res = ops[op._type](res, factor(tok_stream))
    return res


def factor(tok_stream) -> Node:
    tok = tok_stream.peek()
    if tok._type == "LPAREN":
        res = expr(tok_stream)
        # tok_stream.next()
        tok_stream.expect("RPAREN")
    else:
        res = Number(tok_stream.expect("NUM"))
    return res


class TokenStream:
    def __init__(self, iterator: Iterator[Token]):
        self._iterator = iter(iterator)
        self.next()

    def peek(self) -> Token:
        return self._tok

    def expect(self, tok: Token = "LPAREN") -> Token:
        if self._tok != tok:
            raise SyntaxError(f"Expected {tok}")
        res = self._tok
        self.next()
        return res.val  # value of a token

    def next(self) -> None:
        self._tok = next(self._iterator, None)


def parse(text_: str) -> Node:
    # return Plus(left=Number(23), right=Mul(left=Number(42), right=Number(10)))
    tok_stream = TokenStream(tokens_iter(text_))
    res = expr(tok_stream)
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # res = expr(TokenStream(tokens_iter(input_str)))
    # print(res)
