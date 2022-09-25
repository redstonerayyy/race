import os

# generates argsparser and args variables
from util import readfile
from buildargs import getargs
from lexer import Lexer
from parser import Parser

# get command line arguments
args = getargs()

# read main configuration file
racefilepath = os.path.join(args.src, "main.race")

mainfilecontent = readfile(racefilepath)


if mainfilecontent != None:
    # lex main configuration
    tokens = Lexer(mainfilecontent).start()
    # parse main configuration
    tokenparser = Parser(tokens)
    tokenparser.parse()
    print(tokens)
else:
    print(f"Error reading {racefilepath}, a configuration file is required!")

# parse configuration