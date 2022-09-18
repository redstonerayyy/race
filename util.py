from tokenize import String


def readfile(filename) -> String:
        # get file as string
    try:
        with open(filename,"r") as racefile:
            content = racefile.readlines()
            lines = []

            # remove newlines so strings are clean later on
            for line in content:
                lines.append(line.strip(" \n"))

            return lines

    except IOError:
        return None
