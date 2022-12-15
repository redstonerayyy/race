import argparse

def getargs() -> argparse.Namespace:
    # create parser
    argsparser = argparse.ArgumentParser()

    # add arguments
    argsparser.add_argument(
        '-B',
        dest='build', default="./build",
        help='build directory, a relative path'
    )

    argsparser.add_argument(
        '-S',
        dest='src', default="./src",
        help='source directory, a relative path'
    )

    # parse the arguments
    args = argsparser.parse_args()
    return args