class NinjaGenerator:
    def __init__(self, buildvars, instructions) -> None:
        self.buildvars = buildvars
        self.instructions = instructions
        self.filebuffer = ""
        self.filename = "build.ninja"

    def start(self) -> str:
        # generate string for buildvars
        buildstring = ""
        for key in self.buildvars:
            buildstring += key.lower() + " = " + self.buildvars[key] + "\n"
        
        self.filebuffer += buildstring
                