#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import plus_number as PN


class Visitor:
    def visit(self, node):
        self.name = f"visit_{type(node).__name__.lower()}"
        getattr(self, self.name, self.generic_visit)()

    def generic_visit(self, node):
        raise TypeError(f"No visit method {self.name}")


class Eval(Visitor):
    def visit_plus(self, node):
        return node.left + node.right

    def visit_mul(self, node):
        return node.left * node.right


class Infix(Visitor):
    def visit_plus(self, node):
        return f"(+ {node.left} {node.right})"

    def visit_mul(self, node):
        return f"(* {node.left} {node.right})"


if __name__ == "__main__":
    node = PN.Plus(PN.Number(23), PN.Mul(PN.Number(42), PN.Number(10)))
    visitor = Eval()
    infix = Infix()
    print(eval.visit(node))
    print(infix.infix(node))
