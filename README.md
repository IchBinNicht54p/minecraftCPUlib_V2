# Important

This library is not finished, still working on support for other operands and bin -> hex instructions for hex PROM & icache.

This library is also quite buggy, bug reports are appreciated!

*NOTE*  This library requires the libraries `mcschematic` and `pygame` install them via:

```bash
pip install pygame
pip install mcschematic
```

# Documentation

## Compile

You can compile ffcl programs into 54asm with `compiler.py`

```py
import compiler

c = compiler.Compiler("out.54asm") # create compiler object

with open("your_file.ffcl", "r") as f:
    for line in f:
        c.parse_line(f) # parse each line of your ffcl program

c.write_program()
```

Now you'll have a 54asm file automatically generated from compiling your ffcl code. The next step is to compile the 54asm code into ROM (a binary file) that the CPU simulator can actually read.

To compile the 54asm into ROM, we need to use `minecraftCPUlib.py`

```py
import minecraftCPUlib

cpu = minecraftCPUlib.CPU.OP_1(8, 4, 255, 8, "log") # create CPU object

cpu.compile("out.54asm", "out.rom") # compile out.54asm into out.rom
cpu.init() # initialize the CPU, ready for executing

with open("out.rom", "r") as f:
    cpu.load_program(f.read()) # load the rom into the CPU's instruction memory

cpu.run() # finally, execute the CPU
```

The CPU will convert the ROM into instructions based on it's ISA. More about ISA's later throughout the documentation.
