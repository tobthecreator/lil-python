class VMError(Exception):
    pass

class VM(obj):
    def __init__(self):
        self.frames = []
        self.frame = None
        self.returnVal = None
        self.lastError = None

    def Run(self, code, globals=None, locals=None):
        frame = self.make_frame(code, globals, locals)

        self.runFrame(frame)

