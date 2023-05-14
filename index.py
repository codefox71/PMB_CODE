class Printer:
    def __getitem__(self, text):
        print(text)

class InputReader:
    def __getitem__(self, prompt):
        return input(prompt)

class Calculator:
    def __getitem__(self, expression):
        result = eval(expression)
        return result

class ListProcessor:
    def __getitem__(self, items):
        for item in items:
            print(item)

class FileProcessor:
    def __getitem__(self, filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

class Conditional:
    def __getitem__(self, condition):
        return bool(eval(condition))

class Loop:
    def __getitem__(self, count):
        count = int(count)
        return range(count)

class TypeConverter:
    def __getitem__(self, value):
        if isinstance(value, str):
            return str(value)
        elif isinstance(value, int):
            return int(value)
        else:
            return value

pr = Printer()
inp = InputReader()
calc = Calculator()
listp = ListProcessor()
filep = FileProcessor()
cond = Conditional()
loop = Loop()
convert = TypeConverter()

# Read and interpret the .pmx file
def interpret_pmx_file(filename):
    try:
        with open(filename, "r") as file:
            code = file.read()

            # Remove comments from the code
            code_lines = code.split("\n")
            code_lines = [line.split("#")[0].strip() for line in code_lines]
            code = "\n".join(code_lines)

            exec(code, globals(), locals())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Usage:
interpret_pmx_file("main.pmx")  # Interpret and execute the main.pmx file
