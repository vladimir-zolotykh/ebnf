#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Any
import re
from dataclasses import dataclass

text = "23 + 42 * 10"
symbols = [
    ("NAME", r"[a-zA-Z_][a-zA-Z_0-9]*"),
    ("NUM", r"\d+"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("TIMES", r"\*"),
    ("DIVIDE", r"/"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("EQ", r"="),
    ("WS", r"\s+"),
]


class Node:
    def __init__(self, left, right, value):
        pass


@dataclass
class Token:
    _type: str  # "NAME", "WS", ...
    val: Any  # "foo" for NAME, 10 for NUM


vocab = {}
for name, regex in symbols:
    vocab[name] = rf"(?P<{name}>{regex})"


def make_pattern(dict=vocab):
    return "|".join(vocab.values())


def tokens_iter(input_str):
    pat = make_pattern(vocab)
    for mo in re.finditer(pat, input_str):
        yield Token(mo.lastgroup, mo.group(0))


if __name__ == "__main__":
    for tok in tokens_iter(text):
        print(tok)
