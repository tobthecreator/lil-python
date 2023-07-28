class Interpreter:
    def __init__(self):
        self.stack = []

    def LoadValue(self, number):
        self.stack.append(number)

    def AddTwoValues(self):
        n1 = self.stack.pop()
        n2 = self.stack.pop()
        s = n1 + n2
        self.stack.append(s)

    def StoreName(self, name):
        v = self.stack.pop()
        self.environment[name] = val

    def LoadName(self, name):
        v = self.environment[name]
        self.stack.append(val)

    def parseArgument(self, instruction, argument, exec_obj):
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_NAME", "STORE_NAME"]

        if instruction in numbers:
            argument = exec_obj['numbers'][argument]
        elif instruction in names:
            argument = exec_obj['names'][argument]

        return argument

     def PrintAnswer(self):
        answer = self.stack.pop()
        print(answer)

    def Run(self, exec_obj):
        instructions = exec_obj['instructions']
        numbers = exec_obj['numbers']

        for step in instructions:
            instruction, arg = step

            if instruction == "LOAD_VALUE":
                n = numbers[arg]
                self.LoadValue(n)

            elif instruction == "ADD_TWO_VALUES":
                self.AddTwoValues()

            elif instruction == "PRINT_ANSWER":
                self.PrintAnswer()

            elif instruction == "STORE_NAME":
                self.StoreName(arg)

            elif instruction == "LOAD_NAME":
                self.LoadName(arg)

    def Execute(self, exec_obj):
        instructions = exec_obj['instructions']

        for step in instructions:
            instruction, arg = step
            arg = self.parseArgument(instruction, arg, exec_obj)
            method = getatter(self, instruction)

            if arg is None:
                method()
            else:
                method(arg)


interpreter = Interpreter()

exec_obj = {
  "instructions": [
    ("LOAD_VALUE", 0),
    ("LOAD_VALUE", 1),
    ("ADD_TWO_VALUES", None),
    ("LOAD_VALUE", 2),
    ("ADD_TWO_VALUES", None),
    ("PRINT_ANSWER", None)],
    "numbers": [7, 5, 8] 
}

interpreter.Run(exec_obj)