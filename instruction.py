# class to represent an instruction
from enum import Enum

class OPCODE(Enum):
    ADD = 1
    SUB = 2
    AND = 3
    OR = 4
    LD = 5
    
class Instruction:
    def __init__(self, opcode, dest, src1, src2):
        self.opcode = opcode
        self.dest = dest
        self.src1 = src1
        self.src2 = src2

    def __str__(self):
        return f'{self.opcode}, {self.dest}, {self.src1}, {self.src2}'
    