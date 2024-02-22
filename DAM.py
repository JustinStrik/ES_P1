# This processor supports up to 8 locations (0 – 7) in the data memory. At a time step, it can have up to 8
# tokens. The token format is <address, value>, e.g., <6, 5> implies that memory address 6 has value 5. This is
# shown as Di in Figure 1. We will provide an input file (datamemory.txt) with 8 data tokens that you can use
# to initialize the data memory locations. You can assume that the content of a data memory location can vary
# between 0 – 63

def read_data_memory():

    data_memory = []
    with open('datamemory.txt'):
        for line in open('datamemory.txt'):
            line = line.strip()
            line = line.replace('<', '')
            line = line.replace('>', '')
            line = line.split(',')
            address = int(line[0])
            value = int(line[1])
            data_memory.append((address, value))

    return data_memory