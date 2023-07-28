class Frame(object):
    def __init__(self, code, globals, locals, prevFrame):
        self.code = code
        self.globals = globals
        self.locals = locals
        self.prevFrame = prevFrame
        self.stack = []
        self.lastInstruction = 0
        self.blockStack = []

        if prevFrame:
            self.builtins = prevFrame.builtins
        else:
            self.builtins = locals['__builtins__']
            
            if hasattr(self.builtins, '__dict__'):
                self.builtins = self.builtins.__dict__

        