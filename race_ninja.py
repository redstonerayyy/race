class NinjaGenerator:
    def __init__(self, instructions) -> None:
        self.instructions = instructions
        self.filebuffer = ""
        self.filename = "build.ninja"

    def start(self) -> str:
        # pack variables in dict
        buildvars = {}
        for ins in self.instructions:
            if ins[0] == "assignment":
                buildvars[ins[1]] = ins[3]

        # generate string for buildvars
        buildstring = ""
        for key in buildvars:
            buildstring += key.lower() + " = " + buildvars[key] + "\n"
        
        self.filebuffer += buildstring

        # filter out assignments
        self.instructions = list(filter(lambda ins: ins[0] != "assignment", self.instructions))
        print(self.instructions)
        print(self.filebuffer)
        # loop over remaining instructions
        while self.instructions:
            ins = self.instructions.pop(0)
            if ins[0] == "executable":
                