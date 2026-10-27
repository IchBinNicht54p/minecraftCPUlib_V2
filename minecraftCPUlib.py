from sys import exit

import compiler
import display
import isa


class CPU:
    class OP_1:
        def __init__(
            self,
            cpu_bits: int,
            register_count: int,
            ram_cells: int,
            port_count: int,
            log_path: str,
            log: bool = True,
        ):
            if not cpu_bits % 8:
                pass

            self.bits = 8
            self.ram_cells = ram_cells
            self.register_count = register_count
            self.port_count = port_count
            self.acc = 0
            self.pc = 0

            self.flags = {"zero": False, "cout": False}
            self.ports = []
            self.ram = []
            self.regs = []
            self.isa_cache = []
            self.program = []

            self.isa = isa.Isa(self)
            self.display = None
            self.enable_log = log
            self.max_int = (1 << self.bits) - 1

            self.compiler_operands = 0

        def log(self, txt: str):
            print(f"{txt}")

        def init(self):
            for _ in range(self.ram_cells):
                self.ram.append(0)

            for _ in range(self.register_count):
                self.regs.append(0)

            for _ in range(self.port_count):
                self.ports.append({"i": 0, "o": 0})

            self.log("init:\n")
            self.log(f"CPU bits: {self.bits}")
            self.log(f"CPU flags: {self.flags}")
            self.log(f"CPU registers: {self.register_count}")
            self.log(f"CPU ports: {self.port_count}")
            self.log(f"CPU ram cells: {self.ram_cells}")

            self.load_isa_cache()

        def load_isa_cache(self):
            self.isa_cache = []

            for instruction in sorted(self.isa.isa, key=lambda k: self.isa.isa[k][0]):
                self.isa_cache.append(
                    {
                        "f": self.isa.isa[instruction][2],
                        "n": instruction,
                        "operands": self.isa.isa[instruction][1],
                    }
                )

            self.log(f"loaded {len(self.isa_cache)} instructions into isa_cache")

        def dud(self):
            self.pc += 1

        def load_program(self, program: str):
            i = 0

            while i < len(program):
                bin_ins = compiler.binary(ord(program[i]))
                opcode = int(bin_ins[:5], 2) - 1
                operand = int(bin_ins[5:], 2)

                if opcode >= len(self.isa_cache):
                    exit(
                        f"program byte {i} (value {ord(program[i])}) exceeds isa size {len(self.isa_cache)}"
                    )

                ins = self.isa_cache[opcode]

                if len(program) - i < ins["operands"]:
                    exit(
                        f"program byte {i} requires {ins['operands']} but there are only {len(program) - i} instructions left"
                    )

                args = []

                args.append(operand)

                for j in range(ins["operands"] - 1):
                    args.append(ord(program[i + j + 1]))

                self.program.append([ins["f"], args])
                self.log(f"program += {ins['n']}{args}")

                for j in range(ins["operands"] - 1):
                    self.program.append([self.dud, []])

                    self.log("added dud")

                if ins["operands"] < 2:
                    i += 1
                else:
                    i += ins["operands"]

            self.log(
                f"program length: {len(program)}, instructions: {len(self.program)}"
            )

        def run(self):
            print("executing CPU")

            last_instruction = 0
            last_instruction_repeat = 0

            while self.pc < len(self.program) - 1:
                self.program[self.pc][0](*self.program[self.pc][1])

                if self.pc != last_instruction:
                    last_instruction = self.pc

                    continue

                last_instruction_repeat += 1

                if last_instruction_repeat > 8:
                    exit("same instruction repeated 8 times, quitting")

        def compile(self, input_path: str, output_path: str):
            print(f"compiling {input_path}")

            c = ""

            with open(input_path, "r") as f:
                for line in f:
                    if line.startswith(("#", "\n")) or len(line) < 1:
                        continue

                    l = self.compiler_parse_line(line)
                    c += chr(int(l, 2))

            print(f"compiled {input_path}. writing output at {output_path} {len(c)}B")

            with open(output_path, "w") as f:
                f.write(c)

        def compiler_parse_line(self, line: str) -> str:
            ins = line.split()

            if ins[0].lower() == "opr":
                if self.compiler_operands <= 0:
                    exit(
                        f"error: opr called when {self.compiler_operands + 1} operands are needed"
                    )

                self.compiler_operands -= 1

                return compiler.binary(int(ins[1], 2))

            if self.compiler_operands > 0:
                exit(f"error: {ins[0]} called when OPR needed")

            if not ins[0].lower() in self.isa.isa:
                exit(f"opcode {ins[0].lower()} not found in isa")

            opcode = self.isa.isa[ins[0].lower()]
            self.compiler_operands = opcode[1] - 1

            return compiler.binary(opcode[0], 5) + ins[1]

        def update_flags(self):
            if self.acc >= self.max_int:
                self.flags["cout"] = True

                if self.acc > self.max_int:
                    self.acc -= self.max_int
            else:
                if self.acc == 0:
                    self.flags["zero"] = True
                elif self.acc < 0:
                    self.acc = 0
                    self.flags["zero"] = True
                else:
                    self.flags["zero"] = False

                self.flags["cout"] = False

            self.log(f"Updated flags: {self.flags}")
