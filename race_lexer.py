import string

keywords = [
    "executable",
    "include",
    "files",
]

class Lexer:
    def __init__(self, lexerlines : list) -> None:
        self.lexerlines = lexerlines
        self.index = 0
        self.ignorewhitespace = True
        self.buffer = ""
        self.tokens = []

    def start(self) -> list[list[str]]:
        for line in self.lexerlines:
            try:
                while True:
                    self.match(line[self.index])

            except: IndexError

            # terminate add line ending and reset index for next line
            self.terminate()
            self.index = 0
            
        return self.tokens[:]

    
    def next(self) -> None:
        self.index += 1

    def iswhitespace(self, char : string) -> bool:
        return str.isspace(char)

    def isbrace(self, char : string) -> bool:
        return char in ["{", "}"]

    def isquotation(self, char : string) -> bool:
        return char == '"'

    def terminate(self) -> None:
        # terminate identifier literals if buffer is not empty
        if len(self.buffer) > 0:
            self.tokens.append([
                "string" if not(self.buffer in keywords) else "keyword",
                self.buffer
            ])
            self.buffer = ""

    def match(self, char : string) -> None:
        if self.iswhitespace(char) and self.ignorewhitespace:
            self.terminate()

        elif self.isbrace(char):
            self.terminate()
            
            # punctuation
            self.tokens.append([
                "punctuation",
                char
            ])

        elif self.isquotation(char):
            if self.ignorewhitespace:
                self.ignorewhitespace = False
            else:
                self.ignorewhitespace = True
                self.terminate()

        elif char == ",":
            self.terminate()

            # punctuation
            self.tokens.append([
                "punctuation",
                char
            ])

        elif char == "=":
            self.terminate()

            # operator
            self.tokens.append([
                "operator",
                char
            ])

        else: # is just a character, add to buffer
            self.buffer += char

        # progress to next char
        self.next()
