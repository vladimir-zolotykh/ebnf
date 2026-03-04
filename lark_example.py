#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from lark import Lark, Transformer

# Define a grammar for arithmetic
grammar = """
    ?start: expr

    ?expr: expr "+" term   -> add
         | expr "-" term   -> sub
         | term

    ?term: term "*" factor -> mul
         | term "/" factor -> div
         | factor

    ?factor: NUMBER        -> number
           | "(" expr ")"

    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""


# Transformer to evaluate the parsed tree
class Calculate(Transformer):
    def number(self, n):
        return int(n[0])

    def add(self, items):
        return items[0] + items[1]

    def sub(self, items):
        return items[0] - items[1]

    def mul(self, items):
        return items[0] * items[1]

    def div(self, items):
        return items[0] / items[1]


# Create parser
parser = Lark(grammar, parser="lalr", transformer=Calculate())

# Example usage
if __name__ == "__main__":
    text = "23 + 42 * 10"
    result = parser.parse(text)
    print(result)  # Output: 443
