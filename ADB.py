import instruction

class ADB:
    instr = None

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.instr}'
    
    def get_ADB_string(self):
        if self.instr is None:
            return 'ADB:'
        return 'ADB:<' + str(self.instr.opcode) + ',' + str(self.instr.dest) + ',' + str(self.instr.src1) + ',' + str(self.instr.src2) + '>'
    
    # def load(self, instr):
    #     self.instr = instr
    #     return self.instr

    # def is_empty(self):
    #     return self.instr is None

    # def clear(self):
    #     self.instr = None
    #     return self.instr

    # def get_instr(self):
    #     return self.instr