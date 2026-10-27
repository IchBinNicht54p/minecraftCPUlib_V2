from sys import exit

import minecraftCPUlib

# ISA for 1op CPU


class Isa:
    def __init__(self, cpu: minecraftCPUlib.CPU.OP_1):
        self.cpu: minecraftCPUlib.CPU.OP_1 = cpu

        # isa: list[index: int, operand cound: int, method: function]

        self.isa = {
            "ldi": [1, 2, self.LDI],
            "rld": [2, 1, self.RLD],
            "rst": [3, 1, self.RST],
            "inc": [4, 1, self.INC],
            "dec": [5, 1, self.DEC],
            "add": [6, 1, self.ADD],
            "sub": [7, 1, self.SUB],
            "xor": [8, 1, self.XOR],
            "xnor": [9, 1, self.XNOR],
            "and": [10, 1, self.AND],
            "nand": [11, 1, self.NAND],
            "or": [12, 1, self.OR],
            "nor": [13, 1, self.NOR],
            "pst": [14, 1, self.PST],
            "pld": [15, 1, self.PLD],
            "mst": [16, 2, self.MST],
            "mld": [17, 2, self.MLD],
            "jmp": [18, 2, self.JMP],
            "brc": [19, 2, self.BRC],
        }

    def LDI(self, _: int, value: int):
        self.cpu.acc = value
        self.cpu.pc += 1
        self.cpu.log(f"loading immediate {value}")
        self.cpu.update_flags()

    def RLD(self, address: int):
        self.cpu.acc = self.cpu.regs[address]
        self.cpu.pc += 1
        self.cpu.log(f"loaded register {address} into acc")

    def RST(self, address: int):
        self.cpu.regs[address] = self.cpu.acc
        self.cpu.pc += 1
        self.cpu.log(f"saved acc into register {address}")

    def INC(self, _: int):
        self.cpu.acc += 1
        self.cpu.pc += 1
        self.cpu.log("incrementing acc")
        self.cpu.update_flags()

    def DEC(self, _: int):
        self.cpu.acc -= 1
        self.cpu.pc += 1
        self.cpu.log("decrementing acc")
        self.cpu.update_flags()

    def ADD(self, register_address: int):
        self.cpu.acc += self.cpu.regs[register_address]
        self.cpu.pc += 1
        self.cpu.log(f"add reg {register_address}")
        self.cpu.update_flags()

    def SUB(self, register_address: int):
        self.cpu.acc -= self.cpu.regs[register_address]
        self.cpu.pc += 1
        self.cpu.log(f"sub reg {register_address}")
        self.cpu.update_flags()

    def XOR(self, register_address: int):
        self.cpu.acc ^= self.cpu.regs[register_address]
        self.cpu.pc += 1
        self.cpu.log(f"xor reg {register_address}")
        self.cpu.update_flags()

    def XNOR(self, register_address: int):
        self.cpu.acc ^= ~self.cpu.regs[register_address]
        self.cpu.pc += 1
        self.cpu.log(f"xnor reg {register_address}")
        self.cpu.update_flags()

    def AND(self, register_address: int):
        self.cpu.acc &= self.cpu.regs[register_address]
        self.cpu.pc += 1
        self.cpu.log(f"and reg {register_address}")
        self.cpu.update_flags()

    def NAND(self, register_address: int):
        self.cpu.acc &= ~self.cpu.regs[register_address]
        self.cpu.pc += 1
        self.cpu.log(f"nand reg {register_address}")
        self.cpu.update_flags()

    def OR(self, register_address: int):
        self.cpu.acc |= self.cpu.regs[register_address]
        self.cpu.pc += 1
        self.cpu.log(f"or reg {register_address}")
        self.cpu.update_flags()

    def NOR(self, register_address: int):
        self.cpu.acc |= ~self.cpu.regs[register_address]
        self.cpu.pc += 1
        self.cpu.log(f"nor reg {register_address}")
        self.cpu.update_flags()

    def PST(self, address: int):
        self.cpu.ports[address]["o"] = self.cpu.acc
        self.cpu.pc += 1
        self.cpu.log(f"loading acc value to port {address}")

    def PLD(self, address: int):
        self.cpu.acc = self.cpu.ports[address]["i"]
        self.cpu.pc += 1
        self.cpu.log(f"loading port {address} into acc")
        self.cpu.update_flags()

    def MST(self, _: int, address: int):
        self.cpu.ram[address] = self.cpu.acc
        self.cpu.pc += 1
        self.cpu.log(f"storing acc into ram addr {address}")

    def MLD(self, _: int, address: int):
        self.cpu.acc = self.cpu.ram[address]
        self.cpu.pc += 1
        self.cpu.log(f"loading ram addr {address} into acc")

    def JMP(self, _: int, address: int):
        self.pc = address
        self.cpu.log(f"jumping to addr {address}")

    def BRC(self, flag: int, address: int):
        f = ""

        match flag:
            case 0:
                f = "zero"
            case 1:
                f = "cout"
            case _:
                exit(f"error: flag {flag} does not exist")

        self.cpu.log(f"branch {flag}?")

        if self.cpu.flags[f]:
            self.pc = address

            self.cpu.log(f"branch {address}")
        else:
            self.cpu.pc += 1
