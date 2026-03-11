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


class UniqueUnderscoreMeta(type):
    def __new__(mcls, name, bases, namespace):
        counter = 1
        new_namespace = {}
        for attr_name, attr_val in namespace.items():
            if attr_name == "_":
                # rename to _1, _2, ...
                new_namespace[f"_{counter}"] = attr_val
                counter += 1
            else:
                new_namespace[attr_name] = attr_val
        return super().__new__(mcls, name, bases, new_namespace)


def inject_visitors(cls):
    # for name, obj in list(cls.__dict__.items()):
    for obj in list(cls.__dict__.values()):
        if hasattr(obj, "_node_type"):
            # node_type = getattr(obj, "_node_type")
            node_type = obj._node_type
            print(f"{node_type = }")
            setattr(cls, f"visit_{node_type}", obj)
    return cls


def register(node_type):
    def deco(func):
        type_name = node_type.__name__.lower()
        func_name = f"_{type_name}"
        func._node_type = type_name
        func.__name__ = func_name
        return func

    return deco


@inject_visitors
class Eval(Visitor, metaclass=UniqueUnderscoreMeta):
    @register(PN.Number)
    def _1(self, node):
        return node._val

    @register(PN.Plus)
    def _2(self, node):
        return self.visit(node._left) + self.visit(node._right)

    @register(PN.Mul)
    def _3(self, node):
        return self.visit(node._left) * self.visit(node._right)


@inject_visitors
class Infix(Visitor, metaclass=UniqueUnderscoreMeta):
    @register(PN.Number)
    def _1(self, node):
        return str(node._val)

    @register(PN.Plus)
    def _2(self, node):
        return f"(+ {self.visit(node._left)} {self.visit(node._right)})"

    @register(PN.Mul)
    def _3(self, node):
        return f"(* {self.visit(node._left)} {self.visit(node._right)})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
