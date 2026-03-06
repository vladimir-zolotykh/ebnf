#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from __future__ import annotations


class Node:
    def __init__(self, left: Node, right: Node, val: float | str):
        self._left = left
        self._right = right
        self._valf = val


class BinaryOperator(Node):
    pass


class Plus(BinaryOperator):
    pass


class Minus(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class UnaryOperator(Node):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    pass
