from lib2to3.pgen2 import token
import os

# generates argsparser and args variables
from util import readfile
from buildargs import getargs
from lexer import Lexer

# get command line arguments
args = getargs()

# read main configuration file
racefilepath = os.path.join(args.src, "main.race")

mainfilecontent = readfile(racefilepath)

# lex main configuration
if mainfilecontent != None:
    tokens = Lexer(mainfilecontent).start()
    print(tokens)
else:
    print(f"Error reading {racefilepath}, a configuration file is required!")
