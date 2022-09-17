import string

class Parser:
    def __init__(self, parsestring : string) -> None:
        self.parsestring = parsestring
        self.index = 0
        self.buffer = ""
        self.bufferedliterals = []
        self.bracketlist = []

        self.symbols = []
        self.targets = []

    def next(self):
        self.index += 1

    def match(self, char : string):
        if self.iswhitespace(char):
            if len(self.buffer) > 0 and char == " ":
                self.bufferedliterals.append(self.buffer + char)
                self.buffer = ""

        elif self.isbrace(char):
            

        elif char == ",":


        else: # is just a character
            self.buffer += char

        self.next()

    def iswhitespace(self, char : string) -> bool:
        return char == string.whitespace

    def isbrace(self, char : string) -> bool:
        return char in ["{", "}"]