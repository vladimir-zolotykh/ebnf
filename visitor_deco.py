#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> node = PN.Plus(PN.Number(23), PN.Mul(PN.Number(42), PN.Number(10)))
>>> evaluator = Eval()
>>> infix = Infix()
>>> evaluator.visit(node)
443
>>> infix.visit(node)
'(+ 23 (* 42 10))'
"""
from functools import singledispatchmethod
import plus_number as PN


class Visitor:
    def visit(self, node):
        self.name = f"visit_{type(node).__name__.lower()}"
        return getattr(self, self.name, self.generic_visit)(node)

    def generic_visit(self, node):
        raise TypeError(f"No visit method {self.name}")


class Eval(Visitor):
    @singledispatchmethod
    def visit(self, node):
        return super().visit(node)

    @visit.register(PN.Number)
    def _(self, node):
        return node._val

    @visit.register(PN.Plus)
    def _(self, node):
        return self.visit(node._left) + self.visit(node._right)

    @visit.register(PN.Mul)
    def _(self, node):
        return self.visit(node._left) * self.visit(node._right)


class Infix(Visitor):
    @singledispatchmethod
    def visit(self, node):
        return super().visit(node)

    @visit.register(PN.Number)
    def _(self, node):
        return str(node._val)

    @visit.register(PN.Plus)
    def _(self, node):
        return f"(+ {self.visit(node._left)} {self.visit(node._right)})"

    @visit.register(PN.Mul)
    def _(self, node):
        return f"(* {self.visit(node._left)} {self.visit(node._right)})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
