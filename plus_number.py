#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from __future__ import annotations


class Node:
    def __init__(self, left: Node, right: Node, val: float | str):
        self._left = left
        self._right = right
        self._val = val


class BinaryOperator(Node):
    def __init__(self, *args, **kwargs):
        kwargs.update({"val": self.operator})
        super().__init__(*args, **kwargs)


class Plus(BinaryOperator):
    operator = "+"


class Minus(BinaryOperator):
    operator = "-"


class Mul(BinaryOperator):
    operator = "*"


class Div(BinaryOperator):
    operator = "/"


class UnaryOperator(Node):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    pass


def parse(text_: str) -> Node:
    # fmt: off
    return (
        Plus(
            Number("23"),
            Mul(
                Number("42"),
                Number("10"))
        )
    )
    # fmt: on
