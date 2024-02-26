from instruction import Instruction

class INB:
    instr = None

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.instr}'
    
    def get_INB_string(self):
        if self.instr is None:
            return 'INB:'
        # return 'INB:<' + self.instr.opcode + ',' + self.instr.dest + ',' + self.instr.src1 + ',' + self.instr.src2 + '>'
        #         # an only concatenate str (not "int") to str
        #   File "/Users/justin/repos/embedded systems/ES_P1/INB.py", line 15, in get_INB_string
        #     return 'INB:<' + self.instr.opcode + ',' + self.instr.dest + ',' + self.instr.src1 + ',' + self.instr.src2 + '>'
        # make the same return function but with str()
        return 'INB:<' + str(self.instr.opcode) + ',' + str(self.instr.dest) + ',' + str(self.instr.src1) + ',' + str(self.instr.src2) + '>'

    def is_instr_arith(self):
        # if instr is AND, OR, ADD, SUB
        if (self.instr.opcode == 'ADD' or self.instr.opcode == 'SUB' or self.instr.opcode == 'AND' or self.instr.opcode == 'OR'):
            return True
        return False
        
    def set_instr(self, instr):
        self.instr = instr
        return self.instr