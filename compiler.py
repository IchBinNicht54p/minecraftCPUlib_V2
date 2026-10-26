import sys
from enum import Enum


class CompilerMode(Enum):
    DEFAULT = 0
    FUNCTION = 1


def get_datatype(code: str, identifier=":"):
    return code.split(identifier)[0]


def binary(value: int, zeroes=8):
    return bin(value)[2:].zfill(zeroes)


class Compiler:
    def __init__(self, path="out.54asm"):
        self.constants = {}
        self.variables = {}
        self.functions = {}

        self.mode = CompilerMode.DEFAULT
        self.current_function = ""
        self.program_init = []
        self.program = []

        self.program_flag_init_end = 0
        self.program_flag_variable_index = 0

        self.path = path

    def error(self, msg="error"):
        sys.exit(f"error: {msg}")

    def warn(self, msg="warn"):
        print(f"warning: {msg}")

    def parse_datatype(self, code: str, identifier=":") -> int:
        code_split = code.split(identifier)
        datatype = code_split[0]
        value = code_split[1]

        match datatype:
            case "int":
                return int(value)
            case "const":
                if not value in self.constants:
                    self.error(f"constant {value} does not exist")

                return int(self.constants[value])
            case "var":
                if not value in self.variables:
                    self.error(f"variable {value} does not exist")

                return int(self.variables[value]["m"])
            case "program":
                return self.get_program_flag(value)
            case "function":
                if not value in self.functions:
                    self.error(f"function {value} does not exist")

                return self.functions[value]["addr"]
            case "function_end":
                return self.get_function_end(value)
            case _:
                self.error(f"no such datatype as {datatype}")

    def parse_line(self, line: str):
        code = line.split()

        if (
            len(code) < 1
            or len(code[0].replace(" ", "")) < 1
            or code[0].startswith("#")
        ):
            return

        match code[0]:
            case "var":
                v = "00000000"

                if not len(code) <= 2:
                    v = self.parse_datatype(code[3])

                self.create_variable(code[1], v)
            case "const":
                self.create_constant(code[1], self.parse_datatype(code[3]))
            case "end_init":
                self.end_init()
            case "function_end":
                self.end_function()
            case "function":
                if len(code) <= 1:
                    self.error("function needs name")

                self.create_function(code[1])
            case "or" | "nor" | "xor" | "xnor" | "and" | "nand" | "add" | "sub":
                if len(code) <= 2:
                    self.error("bitwise needs at least 2 arguements")

                self.math(code[0], code[1], code[2])
            case "set_port":
                if len(code) <= 2:
                    self.error("too few arguements for set_port")

                self.get_value(code[2], -1)
                self.add_instruction(f"PST {binary(self.parse_datatype(code[1]))}")
            case "jump":
                if len(code) <= 1:
                    self.error("too few arguements for jump")

                self.add_instruction(f"JMP {binary(self.parse_datatype(code[1]))}")
            case "if":
                if len(code) <= 4:
                    self.error("too few arguements for if statement")

                self.handle_condition(code[1], code[3], code[2], code[4])
            case _:
                self.warn(f"unknown keyword {code[0]}")

    def handle_condition(self, a: str, b: str, con: str, addr: str):
        match con:
            case ">":
                self.math("sub", b, a)
                self.add_instruction(f"BRC 001 {binary(self.parse_datatype(addr))}")
            case "<":
                self.math("sub", a, b)
                self.add_instruction(f"BRC 001 {binary(self.parse_datatype(addr))}")
            case "==":
                self.math("sub", a, b)
                self.add_instruction(f"BRC 000 {binary(self.parse_datatype(addr))}")

    def add_instruction(self, instruction: str):
        if self.mode == CompilerMode.FUNCTION:
            self.functions[self.current_function]["code"].append(instruction)

            return

        self.program.append(instruction)

    def get_value(self, code: str, reg: int):
        match get_datatype(code):
            case "var":
                self.add_instruction(f"MLD {binary(self.parse_datatype(code))}")
            case _:
                self.add_instruction(f"LDI {binary(self.parse_datatype(code))}")

        if reg < 0:
            return

        self.add_instruction(f"RST {binary(reg, 3)}")

    def math(self, operation: str, a: str, b: str):
        self.get_value(a, 0)
        self.get_value(b, -1)
        self.add_instruction(f"{operation.upper()} 000")

    def create_variable(self, name: str, value):
        if name in self.variables:
            self.warn(f"redefinition of variable {name}")

        self.variables[name] = {"v": value, "m": self.program_flag_variable_index}
        self.program_flag_variable_index += 1

    def create_constant(self, name: str, value):
        if name in self.constants:
            self.error(f"redefinition of constant {name}")

        self.constants[name] = value

        print(f"creating constant {name} with value {binary(value)}")

    def create_function(self, name: str):
        if name in self.functions:
            self.warn(f"redefinition of function {name}")

        self.current_function = name
        self.functions[name] = {"addr": 0, "code": []}
        self.mode = CompilerMode.FUNCTION

    def end_function(self):
        if self.mode != CompilerMode.FUNCTION:
            self.warn("end_function called outside of function scope")

            return

        self.mode = CompilerMode.DEFAULT
        code = self.functions[self.current_function]["code"]
        address = len(self.program) + self.program_flag_variable_index
        self.functions[self.current_function]["addr"] = address

        self.add_instruction(
            f"JMP {binary(self.get_function_end(self.current_function))}"
        )

        for line in code:
            self.add_instruction(f"{line}")

        print(
            f"creating function {self.current_function} at address {address} with {len(code)} instructions"
        )

    def get_function_end(self, function: str) -> int:
        if not function in self.functions:
            self.error(f"function {function} not found")

        return (
            self.functions[function]["addr"] + len(self.functions[function]["code"]) + 1
        )

    def get_program_flag(self, flag: str):
        variables = vars(self)
        f = f"program_flag_{flag}"

        if not f in variables:
            self.error(f"program flag {f}({flag}) does not exist")

        return variables[f]

    def end_init(self):
        for var in self.variables:
            v = binary(self.variables[var]["v"])
            m = self.variables[var]["m"]

            print(f"creating variable {var} with value {v} at 0x{hex(m)[2:].zfill(8)}")

            self.program_init.append(f"LDI {v}")
            self.program_init.append(f"MST {binary(m)}")

        self.program_flag_init_end = len(self.program_init)

        print(f"program init end at instruction {self.program_flag_init_end}")

    def write_program(self):
        print(
            f"writing {len(self.program) + self.program_flag_variable_index} instructions"
        )

        with open(self.path, "w") as f:
            f.writelines("# init\n\n")
            f.writelines(f"{line}\n" for line in self.program_init)
            f.writelines("\n# program\n\n")
            f.writelines(f"{line}\n" for line in self.program)
