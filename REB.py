from register import Register

class REB:
    registers = []

    def __init__(self):
        pass

    def get_REB_string(self):
        str = 'REB:'
        for register in self.registers:
            str += f'{register.name},{register.value}'
            if register != self.registers[-1]:
                str += ','
        return str

            