# This processor supports up to 8 locations (0 – 7) in the data memory. At a time step, it can have up to 8
# tokens. The token format is <address, value>, e.g., <6, 5> implies that memory address 6 has value 5. This is
# shown as Di in Figure 1. We will provide an input file (datamemory.txt) with 8 data tokens that you can use
# to initialize the data memory locations. You can assume that the content of a data memory location can vary
# between 0 – 63


class DAM:

    locations = []

    def __init__(self):
        self.read_data_memory()

    def __str__(self):
        return f'{self.locations}'
    
    def read(self, address):
        return self.locations[address][1]
    
    def read_data_memory(self):
        # open datamemory.txt and read input in format
        # <0,2>
        # <1,4>
        with open('datamemory.txt'):
            for line in open('datamemory.txt'):
                line = line.strip()
                line = line.replace('<', '')
                line = line.replace('>', '')
                line = line.split(',')
                address = int(line[0])
                value = int(line[1])
                self.locations.append((address, value))

    def get_DAM_string(self):
        # format: DAM:<0,2>,<1,4>,<2,6>,<3,8>,<4,10>,<5,12>,<6,14>,<7,16>
        str = 'DAM:'
        for i in range(len(self.locations)):
            str += f'<{self.locations[i][0]},{self.locations[i][1]}>'
            if i < len(self.locations) - 1:
                str += ','
        return str

        
    