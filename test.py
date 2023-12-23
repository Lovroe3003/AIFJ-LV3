import re
from operators import is_operator
from keywords import is_keyword
from separator import isSeparator
from comment import isComment
from constant import isConstant
from pathlib import Path
from collections import Counter

filepath = Path(__file__).parent / "primjerKoda.txt"
file = open(filepath, "r")

lines = file.readlines()

keywordRegex = re.compile(r"\b(if|else|while|for|return|break|continue)\b")
identifierRegex = re.compile(r"\b[a-zA-Z_]\w*\b")
operatorRegex = re.compile(r"[+-/*=<>%!&|^]")
separatorRegex = re.compile(r"[(),{}:;]")

tokens = []

pos = 0

input = "if (x < 5) { x = x + 1; }"

while pos < len(lines):
    keywordMatch = keywordRegex.match(str(lines), pos)
    identifierMatch = identifierRegex.match(str(lines), pos)
    operatorMatch = operatorRegex.match(str(lines), pos)

print(keywordMatch)
print(identifierMatch)
print(operatorMatch)