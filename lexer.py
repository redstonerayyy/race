import string

tokentypes = [
    "identifier",
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

class Lexer:
    def __init__(self, lexerlines : string) -> None:
        self.lexerlines = lexerlines
        self.index = 0
        self.buffer = ""
        self.tokens = []

    def start(self):
        for line in self.lexerlines:
            try:
                while line[self.index]:
                    self.match(line[self.index])

            except: IndexError

            # terminate add line ending and reset index for next line
            self.terminate()
            self.index = 0
            
        return self.tokens[:]

    
    def next(self):
        self.index += 1

    def iswhitespace(self, char : string) -> bool:
        return str.isspace(char)

    def isbrace(self, char : string) -> bool:
        return char in ["{", "}"]

    def terminate(self):
        # terminate identifier literals if buffer is not empty
        if len(self.buffer) > 0:
            self.tokens.append([
                tokentypes[0] if not(self.buffer in keywords) else tokentypes[3],
                self.buffer
            ])
            self.buffer = ""

    def match(self, char : string):
        if self.iswhitespace(char):
            self.terminate()

        elif self.isbrace(char):
            self.terminate()
            
            # punctuation
            self.tokens.append([
                tokentypes[2],
                char
            ])

        elif char == ",":
            self.terminate()

            # punctuation
            self.tokens.append([
                tokentypes[2],
                char
            ])

        elif char == "=":
            self.terminate()

            # operator
            self.tokens.append([
                tokentypes[1],
                char
            ])

        else: # is just a character, add to buffer
            self.buffer += char

        # progress to next char
        self.next()
