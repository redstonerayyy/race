import os

# generates argsparser and args variables
import buildargs
from util import readfile
from buildargs import getargs

# get command line arguments
args = getargs()

# read main configuration file
racefilepath = os.path.join(args.src, "main.race")

mainfilecontent = readfile(racefilepath)

if mainfilecontent != None:
    mainconfig = parseconfig(mainfilecontent)
else:
    print(f"Error reading {racefilepath}, a configuration file is required!")
