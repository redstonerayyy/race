# rules
rules = """
rule cxx
    command = $cxx -MMD -MT $out -MF $out.d $cflags $includedir -c $in -o $out
    description = CXX $out
    depfile = $out.d
    deps = gcc

rule link
    command = $cxx $ldflags -o $out $in $libs
    description = LINK $out
"""

class NinjaGenerator:
    def __init__(self, buildvars, targets) -> None:
        self.buildvars = buildvars
        self.targets = targets
        self.filebuffer = ""
        self.filename = "build.ninja"

    def start(self) -> str:
        # generate string for buildvars
        buildstring = ""
        for key in self.buildvars:
            buildstring += key.lower() + " = " + self.buildvars[key] + "\n"

        # parse targets
        for target in self.targets:
            if target["type"] == "executable":
                includepaths = []
                filebuildpaths = []
                for child in target["childs"]:
                    if child["name"] == "include":
                        if "childs" in child:
                            for ipath in child["childs"]:
                                includepaths.append("-I" + ipath[1])

                    elif child["name"] == "files":
                        if "childs" in child:
                            for buildpath in child["childs"]:
                                filebuildpaths.append([
                                    buildpath[1],
                                    "".join(buildpath[1].split(".")[:-1]) + ".o"
                                ])

            # write paths
            buildcommands = ["build " + path[1] + ": cxx " + path[0] for path in filebuildpaths]
            allouts = [pathpair[1] for pathpair in filebuildpaths]
            buildcommands.append("build " + target["name"] + ": link " + " ".join(allouts))
            commands = "\n\n".join(buildcommands) + "\n"

            # make string
            # variables
            self.filebuffer += buildstring

            if includepaths:
                self.filebuffer += "includedir = " + "".join(includepaths)

            self.filebuffer += "\n"

            # add rules
            self.filebuffer += rules + "\n"

            # add build commands
            self.filebuffer += commands

        with open("build.ninja", "w") as file:
            file.write(self.filebuffer)