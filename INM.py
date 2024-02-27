# he processor to be simulated only supports five types of instructions: add (ADD), subtract (SUB), logical
# and (AND), logical or (OR), and load (LD). At a time step, the place denoted as Instruction Memory (INM)
# can have up to 16 instruction tokens. This is shown as Ii in Figure 1. We will provide an input file
# (instructions.txt) with up to 16 instruction tokens. It supports the following instruction format. Please note
# that both source operands are always registers.
# <Opcode>, <Destination Register>, <First Source Operand>, <Second Source Operand>
# Sample instruction tokens and equivalent functionality are shown below:
# <ADD, R1, R2, R3> ➔ R1 = R2 + R3
# <SUB, R1, R2, R3> ➔ R1 = R2 – R3
# <AND, R1, R2, R3> ➔ R1 = R2 & R3
# <OR, R1, R2, R3> ➔ R1 = R2 | R3
# <LD, R1, R2, R3> ➔ R1 = DataMemory[R2+R3]

# enum for the different opcodes
from instruction import Instruction

def read_instructions():
    # format:
    # <ADD,R1,R2,R3>
    # <LD,R4,R2,R3>
    # <AND,R5,R2,R3>
    # <LD,R6,R2,R2>
    # <OR,R1,R3,R2>
    instructions = []
    with open('instructions.txt'):
        for line in open('instructions.txt'):
            line = line.strip()
            line = line.replace('<', '')
            line = line.replace('>', '')
            line = line.split(',')
            opcode = line[0]
            dest = line[1]
            src1 = line[2]
            src2 = line[3]
            instructions.append(Instruction(opcode, dest, src1, src2))

    return instructions

class INM:
    instructions = read_instructions()

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.instructions}'

    def read_instructions(self):
        # open instructions.txt and read input in format
        # <ADD,R1,R2,R3>
        # <LD,R4,R2,R3>
        with open('instructions.txt'):
            for line in open('instructions.txt'):
                line = line.strip()
                line = line.replace('<', '')
                line = line.replace('>', '')
                line = line.split(',')
                opcode = line[0]
                dest = line[1]
                src1 = line[2]
                src2 = line[3]
                self.instructions.append(Instruction(opcode, dest, src1, src2))

    def pop(self):
        return self.instructions.pop(0)
    
    def get_INM_string(self):
        # return in format   # INM:<LD,R4,R2,R3>,<AND,R5,R2,R3>,<LD,R6,R2,R2>,<OR,R1,R3,R2>
        str = 'INM:'
        for instr in self.instructions:
            str += f'<{instr.opcode},{instr.dest},{instr.src1},{instr.src2}>'
            if instr != self.instructions[-1]:
                str += ','
        return str
    
    def is_empty(self):
        return len(self.instructions) == 0
