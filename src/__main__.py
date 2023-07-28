from . import Interpreter

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