from tokenize import String


def readfile(filename) -> String:
        # get file as string
    try:
        with open(filename,"r") as racefile:
            content = racefile.read()
            return content

    except IOError:
        return None
