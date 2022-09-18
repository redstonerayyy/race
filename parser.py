
from lib2to3.pgen2 import token


tokentypes = [
    "string",
    "operator",
    "punctuation",
    "keyword",
]

keywords = [
    "executable",
    "library",
    "include",
    "files",
]

grammartokens = [
    "exp",
    "block"
]

"""
grammar
exp : string '=' string 
    | keyword string block 
    | string

block: '{' exp++ '}'
"""

grammar = [
    [
        ["string", ["operator", "="], "string"],
        "exp"
    ],
    [
        ["keyword", "string", "block"],
        "exp"
    ],
    [
        ["string"],
        "exp"
    ],
    [
        [["punctuation", "{"], ["exp", "++"], ["punctuation", "}"]],
        "block"
    ],
]


class Parser:
    def __init__(self, tokens : list) -> None:
        self.position = 0
        self.tokens = tokens
        self.peek = []
        self.tree = []


    def check_rule(self, rule):
        if len(self.peek) <= len(rule):
            for tokenindex in range(len(self.peek)):
                # check main rule
                if self.peek[tokenindex][0] == rule[tokenindex]:
                    # check sub rule
                    if len(rule[tokenindex]) > 1:
                        if self.peek[tokenindex][1] == "++":

                        elif self.peek[tokenindex][1] == rule[tokenindex][1]:

                        else:

                    else:
                        

    def parse(self):
        while self.position < len(self.tokens):
            self.peek.append(self.tokens[self.position])
            for rule in grammar:
                self.check_rule(rule)
                




