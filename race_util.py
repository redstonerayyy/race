def readfile(filename) -> str:
    # get file as string
    try:
        with open(filename,"r") as racefile:
            # remove newlines so strings are clean later on
            lines = [line.strip(" \n") for line in racefile.readlines()]
            # return array of lines
            return lines

    except IOError:
        return None
