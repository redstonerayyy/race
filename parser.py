from language import *

"""
grammar
exp : string operator["="] string 
    | keyword["executable"] string block
    | string
    | keyword["include, files"] block

block: punctuation["{"] exp++ punctuation["}"]'
"""

grammartokens = [
    "exp",
    "block"
]

grammar = {
    
        "exp":
    [
        [
            ["string", False, False],
            ["operator", ["="], False],
            ["string", False, False],
        ],
        [
            ["keyword", ["executable"], False],
            ["string", False, False],
            ["block", False, False],
        ],
        [
            ["string", False, False],
        ],
        [
            ["keyword", ["include", "files"], False],
            ["block", False, False],
        ]
    ],
    
        "block":
    [
        [
            ["punctuation", ["{"], False, False],
            ["exp", False, True],
            ["punctuation", ["}"], False, False],
        ]
    ],
}


# LL(n) recursive parser

class Parser:
    def __init__(self, tokens : list) -> None:
        self.position = 0
        self.tokens = tokens
        self.buffer = []
        self.expressions = []

    def add(self):
        self.buffer.append(self.tokens[self.position])

    def parse(self):
        while self.position < len(self.tokens):
            if not self.parseExpression():
                return False

    # hand copy of rule to this function
    def compare(self, buffer, rule):
        i = 0
        while i < len(buffer) and i < len(rule):
            # if the next token is another grammar construct, check if the beginnning matches
            if rule[i][0] in grammartokens:
                grammarrules = grammar[rule[i][0]]
                for grule in grammarrules:
                    if (buffer[i][0] == grule[i][0]):
                        if grule[i][1]:
                            if (buffer[i][1] in grule[i][1]):
                                pass
                            else:
                                return False
                        else:
                            pass
                    else:
                        return False
                return True
            # check if the tokens match and if the values, if present, also match
            else:
                if (buffer[i][0] == rule[i][0]):
                    if rule[i][1]:
                        if (buffer[i][1] in rule[i][1]):
                            pass
                        else:
                            return False
                    else:
                        pass
                else:
                    return False
            i += 1
        return True

    def parseExpression(self):
        allmatches = []
        depth = 0
        while True:
            self.add()
            depthmatches = []
            for rule in  grammar["exp"]:
                if self.compare(self.buffer, rule[:]):
                    depthmatches.append(rule[:])
            
            if len(depthmatches) < 2:
                break

            allmatches.append(depthmatches)
            depth += 1

        match = False
        #check which is the hightest depth, were only 1 match is
        for matches in allmatches[::-1]:
            print(matches)
            if len(matches) < 2:
                match = matches[0]
        
        
        # if necessary parse subblocks, else return it and push it onto expression stack
        if match:
            # clear buffer, change position
            self.position += len(match)
            self.buffer = []
            print(match)
        else:
            print("error during parsing")
        return False

        

    # def parseBlock(self):

