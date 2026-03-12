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
import plus_number as PN


class Visitor:
    def visit(self, node):
        self.name = f"visit_{type(node).__name__.lower()}"
        return getattr(self, self.name, self.generic_visit)(node)

    def generic_visit(self, node):
        raise TypeError(f"No visit method {self.name}")


class VisitorDeco:
    _register = {}

    @classmethod
    def inject_visitors(cls, target_cls):
        for node_type, obj in cls._register.items():
            setattr(target_cls, f"visit_{node_type}", obj)
        return target_cls

    @classmethod
    def register(cls, node_type):
        def deco(func):
            type_name = node_type.__name__.lower()
            func._node_type = type_name
            cls._register[type_name] = func
            return func

        return deco


@VisitorDeco.inject_visitors
class Eval(Visitor):
    @VisitorDeco.register(PN.Number)
    def _(self, node):
        return node._val

    @VisitorDeco.register(PN.Plus)
    def _(self, node):
        return self.visit(node._left) + self.visit(node._right)

    @VisitorDeco.register(PN.Mul)
    def _(self, node):
        return self.visit(node._left) * self.visit(node._right)


@VisitorDeco.inject_visitors
class Infix(Visitor):
    @VisitorDeco.register(PN.Number)
    def _(self, node):
        return str(node._val)

    @VisitorDeco.register(PN.Plus)
    def _(self, node):
        return f"(+ {self.visit(node._left)} {self.visit(node._right)})"

    @VisitorDeco.register(PN.Mul)
    def _(self, node):
        return f"(* {self.visit(node._left)} {self.visit(node._right)})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
