# . Register File (RGF):
# This processor supports up to 8 registers (R0 through R7). At a time step, it can have up to 8 tokens. The
# token format is <registername, registervalue>, e.g., <R1, 5>. This is shown as Xi in Figure 1. We will
# provide an input file (registers.txt) with 8 register tokens that you can use to initialize the registers. You can
# assume that the content of a register can vary between 0 – 63.
    
from register import Register

class RGF:
    registers = []

    def __init__(self):
        self.read_registers()
    
    def __str__(self):
        return f'{self.registers}'
    
    def read(self, register):
        for reg in self.registers:
            if reg.name == register:
                return reg.value
    
    def write(self, register, value):
        for reg in self.registers:
            if reg.name == register:
                reg.value = value
                return reg.value
            
    def read_registers(self):
        with open('registers.txt'):
            for line in open('registers.txt'):
                line = line.strip()
                line = line.replace('<', '')
                line = line.replace('>', '')
                line = line.split(',')
                name = line[0]
                value = int(line[1])
                self.registers.append(Register(name, value))

    def get_RGF_string(self):
        # format     # RGF:<R0,4>,<R1,3>,<R2,2>,<R3,1>,<R4,4>,<R5,3>,<R6,2>,<R7,1>

        str = 'RGF:'
        for i in range(len(self.registers)):
            str += f'<{self.registers[i].name},{self.registers[i].value}>'
            if i < len(self.registers) - 1:
                str += ','

        return str
