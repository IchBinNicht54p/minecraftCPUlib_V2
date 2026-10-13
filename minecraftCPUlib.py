import pygame
from mcschematic import MCSchematic, Version
from os import system, remove
from time import sleep

print("Minecraft CPU lib version 1.0(BETA)")

barrels = [
    "minecraft:barrel[facing=up]",
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b},{Slot:10b,id:"minecraft:wooden_axe",Count:1b},{Slot:11b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b},{Slot:10b,id:"minecraft:wooden_axe",Count:1b},{Slot:11b,id:"minecraft:wooden_axe",Count:1b},{Slot:12b,id:"minecraft:wooden_axe",Count:1b},{Slot:13b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b},{Slot:10b,id:"minecraft:wooden_axe",Count:1b},{Slot:11b,id:"minecraft:wooden_axe",Count:1b},{Slot:12b,id:"minecraft:wooden_axe",Count:1b},{Slot:13b,id:"minecraft:wooden_axe",Count:1b},{Slot:14b,id:"minecraft:wooden_axe",Count:1b},{Slot:15b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b},{Slot:10b,id:"minecraft:wooden_axe",Count:1b},{Slot:11b,id:"minecraft:wooden_axe",Count:1b},{Slot:12b,id:"minecraft:wooden_axe",Count:1b},{Slot:13b,id:"minecraft:wooden_axe",Count:1b},{Slot:14b,id:"minecraft:wooden_axe",Count:1b},{Slot:15b,id:"minecraft:wooden_axe",Count:1b},{Slot:16b,id:"minecraft:wooden_axe",Count:1b},{Slot:17b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b},{Slot:10b,id:"minecraft:wooden_axe",Count:1b},{Slot:11b,id:"minecraft:wooden_axe",Count:1b},{Slot:12b,id:"minecraft:wooden_axe",Count:1b},{Slot:13b,id:"minecraft:wooden_axe",Count:1b},{Slot:14b,id:"minecraft:wooden_axe",Count:1b},{Slot:15b,id:"minecraft:wooden_axe",Count:1b},{Slot:16b,id:"minecraft:wooden_axe",Count:1b},{Slot:17b,id:"minecraft:wooden_axe",Count:1b},{Slot:18b,id:"minecraft:wooden_axe",Count:1b},{Slot:19b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b},{Slot:10b,id:"minecraft:wooden_axe",Count:1b},{Slot:11b,id:"minecraft:wooden_axe",Count:1b},{Slot:12b,id:"minecraft:wooden_axe",Count:1b},{Slot:13b,id:"minecraft:wooden_axe",Count:1b},{Slot:14b,id:"minecraft:wooden_axe",Count:1b},{Slot:15b,id:"minecraft:wooden_axe",Count:1b},{Slot:16b,id:"minecraft:wooden_axe",Count:1b},{Slot:17b,id:"minecraft:wooden_axe",Count:1b},{Slot:18b,id:"minecraft:wooden_axe",Count:1b},{Slot:19b,id:"minecraft:wooden_axe",Count:1b},{Slot:20b,id:"minecraft:wooden_axe",Count:1b},{Slot:21b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b},{Slot:10b,id:"minecraft:wooden_axe",Count:1b},{Slot:11b,id:"minecraft:wooden_axe",Count:1b},{Slot:12b,id:"minecraft:wooden_axe",Count:1b},{Slot:13b,id:"minecraft:wooden_axe",Count:1b},{Slot:14b,id:"minecraft:wooden_axe",Count:1b},{Slot:15b,id:"minecraft:wooden_axe",Count:1b},{Slot:16b,id:"minecraft:wooden_axe",Count:1b},{Slot:17b,id:"minecraft:wooden_axe",Count:1b},{Slot:18b,id:"minecraft:wooden_axe",Count:1b},{Slot:19b,id:"minecraft:wooden_axe",Count:1b},{Slot:20b,id:"minecraft:wooden_axe",Count:1b},{Slot:21b,id:"minecraft:wooden_axe",Count:1b},{Slot:22b,id:"minecraft:wooden_axe",Count:1b},{Slot:23b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b},{Slot:10b,id:"minecraft:wooden_axe",Count:1b},{Slot:11b,id:"minecraft:wooden_axe",Count:1b},{Slot:12b,id:"minecraft:wooden_axe",Count:1b},{Slot:13b,id:"minecraft:wooden_axe",Count:1b},{Slot:14b,id:"minecraft:wooden_axe",Count:1b},{Slot:15b,id:"minecraft:wooden_axe",Count:1b},{Slot:16b,id:"minecraft:wooden_axe",Count:1b},{Slot:17b,id:"minecraft:wooden_axe",Count:1b},{Slot:18b,id:"minecraft:wooden_axe",Count:1b},{Slot:19b,id:"minecraft:wooden_axe",Count:1b},{Slot:20b,id:"minecraft:wooden_axe",Count:1b},{Slot:21b,id:"minecraft:wooden_axe",Count:1b},{Slot:22b,id:"minecraft:wooden_axe",Count:1b},{Slot:23b,id:"minecraft:wooden_axe",Count:1b},{Slot:24b,id:"minecraft:wooden_axe",Count:1b},{Slot:25b,id:"minecraft:wooden_axe",Count:1b}]}',
    'barrel[facing=up]{Items:[{Slot:0b,id:"minecraft:wooden_axe",Count:1b},{Slot:1b,id:"minecraft:wooden_axe",Count:1b},{Slot:2b,id:"minecraft:wooden_axe",Count:1b},{Slot:3b,id:"minecraft:wooden_axe",Count:1b},{Slot:4b,id:"minecraft:wooden_axe",Count:1b},{Slot:5b,id:"minecraft:wooden_axe",Count:1b},{Slot:6b,id:"minecraft:wooden_axe",Count:1b},{Slot:7b,id:"minecraft:wooden_axe",Count:1b},{Slot:8b,id:"minecraft:wooden_axe",Count:1b},{Slot:9b,id:"minecraft:wooden_axe",Count:1b},{Slot:10b,id:"minecraft:wooden_axe",Count:1b},{Slot:11b,id:"minecraft:wooden_axe",Count:1b},{Slot:12b,id:"minecraft:wooden_axe",Count:1b},{Slot:13b,id:"minecraft:wooden_axe",Count:1b},{Slot:14b,id:"minecraft:wooden_axe",Count:1b},{Slot:15b,id:"minecraft:wooden_axe",Count:1b},{Slot:16b,id:"minecraft:wooden_axe",Count:1b},{Slot:17b,id:"minecraft:wooden_axe",Count:1b},{Slot:18b,id:"minecraft:wooden_axe",Count:1b},{Slot:19b,id:"minecraft:wooden_axe",Count:1b},{Slot:20b,id:"minecraft:wooden_axe",Count:1b},{Slot:21b,id:"minecraft:wooden_axe",Count:1b},{Slot:22b,id:"minecraft:wooden_axe",Count:1b},{Slot:23b,id:"minecraft:wooden_axe",Count:1b},{Slot:24b,id:"minecraft:wooden_axe",Count:1b},{Slot:25b,id:"minecraft:wooden_axe",Count:1b},{Slot:26b,id:"minecraft:wooden_axe",Count:1b}]}',
]


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


class Schematic:
    def __init__(
        self, compiled_code: list, distance: tuple = (2, 2, 2), max_x: int = 8
    ):
        with open("_temp", "w") as f:
            f.write(compiled_code)

        with open("_temp", "r") as f:
            self.c = f.readlines()

        remove("_temp")

        self.d = distance
        self.s = MCSchematic()
        self.mx = max_x
        self.mx1 = self.mx + 1
        self.z = 0
        self.a = 0
        self.zs = 0
        self.ci = 0

    def binary(self, path: str = "Schematic", x: int = 0, y: int = 0, z: int = 0):
        for ci in range(len(self.c)):
            for bi in range(len(self.c[ci])):
                match self.c[ci][invert(bi, len(self.c[ci]))]:
                    case "1":
                        b = "minecraft:redstone_block"
                    case "0":
                        b = "minecraft:stone"
                    case _:
                        b = "minecraft:air"
                if self.z > 0:
                    self.a = self.d[0]
                    self.mx = self.mx1
                else:
                    self.a = 0
                self.s.setBlock(
                    (
                        ((self.zs * self.d[0]) - self.a) + x,
                        ((y + 1) - (len(self.c[ci]) * self.d[1])) + (bi * self.d[1]),
                        z + (self.z * self.d[2]),
                    ),
                    b,
                )
            if self.zs > self.mx - 2:
                self.z += 1
                self.zs = 0
            self.zs += 1

        self.s.save("", path, Version.JE_1_18_2)

    def hex(self, path: str = "Schematic", x: int = 0, y: int = 0, z: int = 0):
        for ci in range(len(self.c)):
            for bi in range(len(self.c[ci].split())):
                b = barrels[
                    int(self.c[ci].split()[invert(bi, len(self.c[ci].split()))])
                ]
                if self.z > 0:
                    self.a = self.d[0]
                    self.mx = self.mx1
                else:
                    self.a = 0
                self.s.setBlock(
                    (
                        ((self.zs * self.d[0]) - self.a) + x,
                        1
                        + (
                            (x + (bi * self.d[1]))
                            - (len(self.c[ci].split()) * self.d[1])
                        ),
                        z + (self.z * self.d[2]),
                    ),
                    b,
                )
            if self.zs > self.mx - 2:
                self.z += 1
                self.zs = 0
            self.zs += 1

        self.s.save("", path, Version.JE_1_18_2)


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
    class display:
        def __init__(self, pixels: tuple = (255, 255), pixel_size: int = 2):
            self.p = pixels
            self.s = pixel_size
            self.pixel = []

            for _ in range(pixels[0]):
                self.pixel.append([0 for _ in range(pixels[1])])

            pygame.init()

            self.window = pygame.display.set_mode(
                (self.p[0] * self.s, self.p[1] * self.s)
            )

            self.clock = pygame.time.Clock()
            self.run = True

        def draw(self):
            self.window.fill("white")

            for x in range(len(self.pixel)):
                for y in range(len(self.pixel[x])):
                    p = self.pixel[invert(y, len(self.pixel[x]))][x]

                    if p == 0:
                        c = "black"
                    else:
                        c = "white"

                    pygame.draw.rect(
                        self.window, c, (x * self.s, y * self.s, self.s, self.s)
                    )

        def change_pixel(self, pixel: tuple = (0, 0), on: bool = True):
            if pixel[0] <= self.p[0] - 1 and pixel[1] <= self.p[1] - 1:
                if on:
                    self.pixel[pixel[0]][pixel[1]] = 1
                else:
                    self.pixel[pixel[0]][pixel[1]] = 0

        def reset(self):
            for x in range(len(self.pixel)):
                for y in range(len(self.pixel[x])):
                    self.pixel[x][y] = 0

        def start(self, FPS: int = 60):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.draw()
            self.clock.tick(FPS)
            pygame.display.flip()

        def should_run(self):
            return self.run

    class OP_1:
        def __init__(
            self,
            cpu_bits: int,
            register_count: int,
            ram_cells: int,
            port_count: int,
            log_path: str,
            log: bool = True,
            output_ports=False,
            simulation_speed: int = 0,
        ):
            if not cpu_bits % 8:
                pass

            self.bits = 8
            self.acc = 0
            self.alu = 0
            self.flags = {"zero": False, "cout": False}
            self.ram = [0 for _ in range(ram_cells)]
            self.regs = [0 for _ in range(register_count)]
            self.ports = [{"i": 0, "o": 0} for _ in range(port_count)]

            self.max_int = (1 << self.bits) - 1
            self.l = log
            self.sim = []
            self.po = output_ports
            self.s = simulation_speed

            if self.l:
                with open("log.txt", "w") as f:
                    f.write(
                        f"*** init ***:\n\nSuccessfully created a new CPU object.\n\nCPU bits: {self.bits}\nCPU flags: {self.flags}\nCPU registers: {self.regs}\nCPU ports: {self.ports}\nCPU ram cells: {len(self.ram)}\n\n*** execution ***\n\n"
                    )

        def log(self, msg: str):
            with open("log.txt", "a") as f:
                f.write(f"{msg}\n\n")

        def update_flags(self):
            if self.alu >= self.max_int:
                self.flags["cout"] = True
                if self.alu > self.max_int:
                    self.alu -= self.max_int
            else:
                if self.alu == 0:
                    self.flags["zero"] = True
                elif self.alu < 0:
                    self.alu = 0
                    self.flags["zero"] = True
                else:
                    self.flags["zero"] = False
                self.flags["cout"] = False
            self.log(f"Updated flags: {self.flags}")
