import register

class REB:
    registers = []

    def __init__(self):
        pass

    def get_REB_string(self):
        return 'REB:<' + ','.join([str(reg) for reg in self.registers]) + '>'
            