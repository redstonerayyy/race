
tokentypes = [
    "identifier",
    "operator",
    "punctuation",
    "keyword",
]

# how to parse
"""
identifier operator(=) identifier => variables 


"""


class Parser:
    def __init__(self, tokens : list) -> None:
        