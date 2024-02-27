from register import Register

class ADB:
    reg = None

    def __init__(self):
        pass
    
    def get_ADB_string(self):
        if self.reg is None:
            return 'ADB:'
        return 'ADB:<' + str(self.reg.name) + ',' + str(self.reg.value) + '>'
    
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