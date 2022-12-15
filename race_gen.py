# path functions
import os
# generates argsparser and args variables
from race_args import getargs
# read content of file
from race_util import readfile
# lexer to convert string to tokens
from race_lexer import Lexer
# parser to parse tokens to instructions
import race_parser
# generate files for building
from race_ninja import NinjaGenerator

def main() -> None:
    # get command line arguments
    args = getargs()

    # read main configuration file
    racefilepath = os.path.join(args.src, "main.race")
    mainfilecontent = readfile(racefilepath)

    # check if file got read correctly by function
    if mainfilecontent == None:
        print(f"Error reading {racefilepath}, a configuration file is required!")
        
    # lex main configuration
    tokens = Lexer(mainfilecontent).start()
    # print(tokens)
    
    # parse configuration
    instructions = race_parser.Parser(tokens).start()
    # print(instructions)

    # generate build.ninja files
    filecontent = NinjaGenerator(instructions).start()

if __name__ == "__main__":
    main()