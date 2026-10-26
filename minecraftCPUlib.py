from sys import exit

import compiler
import display
import isa


def invert(val: int, max_int: int):
    return (max_int - val) - 1


def bin_bit_5_convert(val: int):
    if val > (1 << 5) - 1:
        val = (1 << 5) - 1

    return f"{val:05b}"


def bin_op_convert(op: int):
    if op > (1 << 3) - 1:
        op = (1 << 3) - 1

    return f"{op:03b}"


def bin_op2_convert(op: int):
    if op > (1 << 8) - 1:
        op = (1 << 8) - 1

    return f"{op:08b}"


def horiz_bin_to_dec(bv: list):
    v = 0

    for d in range(len(bv)):
        if bv[d] == "1":
            v += 1 << invert(d, len(bv))

    return v


def convert_4_bits(bv: list, add: int = 0):
    o = []

    for i in range(len(bv[0])):
        l = []

        for j in range(4):
            l.append(bv[j][i])

        o.append((horiz_bin_to_dec(l) + add))

    o2 = ""

    for i in range(len(o)):
        o2 += f"{o[i]}"

        if i < len(o) - 1:
            o2 += " "

    return o2 + "\n"


class Compile:
    def __init__(self, code: dict, ISA: dict):
        self.isa = ISA
        self.c = code

    def to_binary(self):
        o = ""
        ix = 0

        for i in self.c:
            ins = 0

            for s in self.isa["instructions"]:
                if s == i["id"]:
                    break
                ins += 1

            if i["id"] in ["ldi"]:
                if i["id"] in ["ldi", "jmp"]:
                    o += f"{bin_bit_5_convert(ins)}000\n"
                    o += f"{bin_op2_convert(i['op'])}"
                else:
                    o += f"{bin_bit_5_convert(ins)}{bin_op_convert(i['op'])}\n"
                    fins = 0

                    if i["op"] == 0:
                        f = "zero"
                    elif i["op"] == 1:
                        f = "cout"

                    for fn in self.isa["flags"]:
                        if fn == f:
                            break

                        fins += 1

                    o += f"{bin_op2_convert(fins)}"
            else:
                o += f"{bin_bit_5_convert(ins)}{bin_op_convert(i['op'])}"

            if ix < len(self.c) - 1:
                o += "\n"

            ix += 1

        return o

    def to_hex(self, add: int = 0):
        b = self.to_binary()

        with open("temp", "w") as f:
            f.write(b)

        o = ""
        i = 0

        with open("temp", "r") as f:
            c = f.readlines()
            l = 0

            while l < len(c):
                bl = []

                for i in range(4):
                    try:
                        bl.append(c[i + l][:8])
                    except IndexError:
                        bl.append("0" * 8)

                o += convert_4_bits(bl, add=add)
                l += 4

        remove("temp")  # <-----
        return o


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
            self.log(f"CPU registers: {self.regs}")
            self.log(f"CPU ports: {self.ports}")
            self.log(f"CPU ram cells: {self.ram_cells}")

        def compile(self, input_path: str, output_path: str):
            print(f"compiling {input_path}")

            c = ""

            with open(input_path, "r") as f:
                for line in f:
                    if line.startswith(("#", "\n")) or len(line) < 1:
                        continue

                    l = self.compiler_parse_line(line)

                    for number in l:
                        c += chr(int(number, 2))

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

                return compiler.binary(int(ins[1]))

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
