import instruction

class AIB:
    instr = None

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.instr}'
    
    def get_AIB_string(self):
        if self.instr is None:
            return 'None'
        return 'AIB:<' + self.instr.opcode + ',' + self.instr.dest + ',' + self.instr.src1 + ',' + self.instr.src2 + '>'