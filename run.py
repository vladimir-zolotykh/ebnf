#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

import re

text = "23 + 42 * 10"
symbols = [
    ("NAME", r"[a-zA-Z_][a-zA-Z_0-9]*"),
    ("NUM", r"\d+"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("TIMES", r"\*"),
    ("EQ", r"="),
    ("WS", r"\s+"),
]

vocab = {}
for name, regex in symbols:
    vocab[name] = rf"(?P<{name}>{regex})"


def make_pattern(dict=vocab):
    return "|".join(vocab.values())


def tokens_iter(input_str):
    pat = make_pattern(vocab)
    for tok in re.finditer(pat, input_str):
        yield tok


if __name__ == "__main__":
    for mo in tokens_iter(text):
        print(mo.lastgroup, mo.group(0))

# >>> vocab
# {'NAME': '(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)', 'NUM': '(?P<NUM>\\d+)', 'PLUS': '(?P<PLUS>\\+)', 'MINUS': '(?P<MINUS>-)', 'TIMES': '(?P<TIMES>\\*)', 'EQ': '(?P<EQ>=)', 'WS': '(?P<WS>\\s+)'}
