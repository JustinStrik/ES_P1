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
    
class Register:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'<{self.name}, {self.value}>'
    

class ADB:
    reg = None

    def __init__(self):
        pass
    
    def get_ADB_string(self):
        if self.reg is None:
            return 'ADB:'
        return 'ADB:<' + str(self.reg.name) + ',' + str(self.reg.value) + '>'
    
class AIB:
    instr = None

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.instr}'
    
    def get_AIB_string(self):
        if self.instr is None:
            return 'AIB:'
        return 'AIB:<' + str(self.instr.opcode) + ',' + str(self.instr.dest) + ',' + str(self.instr.src1) + ',' + str(self.instr.src2) + '>'
    
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

class INB:
    instr = None

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.instr}'
    
    def get_INB_string(self):
        if self.instr is None:
            return 'INB:'
        return 'INB:<' + str(self.instr.opcode) + ',' + str(self.instr.dest) + ',' + str(self.instr.src1) + ',' + str(self.instr.src2) + '>'

    def is_instr_arith(self):
        # if instr is AND, OR, ADD, SUB
        if (self.instr.opcode == 'ADD' or self.instr.opcode == 'SUB' or self.instr.opcode == 'AND' or self.instr.opcode == 'OR'):
            return True
        return False
        
    def set_instr(self, instr):
        self.instr = instr
        return self.instr
    

class INM:
    instructions = []
    
    def __init__(self):
        self.read_instructions()

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

class LIB:
    instr = None

    def __init__(self):
        pass

    def __str__(self):
        return f'{self.instr}'
    
    def get_LIB_string(self):
        if self.instr is None:
            return 'LIB:'
        return 'LIB:<' + str(self.instr.opcode) + ',' + str(self.instr.dest) + ',' + str(self.instr.src1) + ',' + str(self.instr.src2) + '>'

class REB:
    registers = []

    def __init__(self):
        pass

    def get_REB_string(self):
        str = 'REB:'
        for register in self.registers:
            str += f'<{register.name},{register.value}>'
            if register != self.registers[-1]:
                str += ','
        return str
    
    def is_empty(self):
        return len(self.registers) == 0
    

class RGF:
    registers = []

    def __init__(self):
        self.read_registers()
    
    def __str__(self):
        return f'{self.registers}'
    
    def read(self, register):
        for reg in self.registers:
            if reg.name == register:
                return reg.value
    
    def write(self, register, value):
        for reg in self.registers:
            if reg.name == register:
                reg.value = value
                return reg.value
            
    def read_registers(self):
        with open('registers.txt'):
            for line in open('registers.txt'):
                line = line.strip()
                line = line.replace('<', '')
                line = line.replace('>', '')
                line = line.split(',')
                name = line[0]
                value = int(line[1])
                self.registers.append(Register(name, value))

    def get_RGF_string(self):
        # format     # RGF:<R0,4>,<R1,3>,<R2,2>,<R3,1>,<R4,4>,<R5,3>,<R6,2>,<R7,1>

        str = 'RGF:'
        for i in range(len(self.registers)):
            str += f'<{self.registers[i].name},{self.registers[i].value}>'
            if i < len(self.registers) - 1:
                str += ','

        return str



INM_has_token, INB_has_token, AIB_has_token, LIB_has_token, ADB_has_token, REB_has_token, RGF_has_token, DAM_has_token = True, False, False, False, False, False, False, False
decode_has_token, read_has_token, ADDR_has_token, load_has_token, write_has_token, issue1_has_token, issue2_has_token, ALU_has_token = False, False, False, False, False, False, False, False

INM_ = INM()
RGF_ = RGF()
DAM_ = DAM()
INB_ = INB()
AIB_ = AIB()
LIB_ = LIB()
ADB_ = ADB()
REB_ = REB()

output = ''
step = 0 # for counting steps in the simulation

def check_for_tokens():
    # is any tokens exist in any of the buffers, return True
    if (INM_has_token or INB_has_token or AIB_has_token or LIB_has_token or ADB_has_token or REB_has_token or RGF_has_token or DAM_has_token or decode_has_token or read_has_token or ADDR_has_token or load_has_token or write_has_token or issue1_has_token or issue2_has_token):
        return True
    else:
        return False
    
def write_output():
    # format:
    # STEP 4:
    # INM:<OR,R1,R3,R2>
    # INB:<LD,R6,2,2>
    # AIB:<AND,R5,2,1>
    # LIB:
    # ADB:<R4,3>
    # REB:
    # RGF:<R0,4>,<R1,3>,<R2,2>,<R3,1>,<R4,4>,<R5,3>,<R6,2>,<R7,1>
    # DAM:<0,2>,<1,4>,<2,6>,<3,8>,<4,10>,<5,12>,<6,14>,<7,16>
    # to a file called simulation
    output = f'STEP {step}:\n'
    output += f'{INM_.get_INM_string()}\n'
    output += f'{INB_.get_INB_string()}\n'
    output += f'{AIB_.get_AIB_string()}\n'
    output += f'{LIB_.get_LIB_string()}\n'
    output += f'{ADB_.get_ADB_string()}\n'
    output += f'{REB_.get_REB_string()}\n'
    output += f'{RGF_.get_RGF_string()}\n'
    output += f'{DAM_.get_DAM_string()}\n'
    output += '\n'

    with open('simulation.txt', 'a') as file:
        file.write(output)

def decode():
    # The DECODE transition consumes the top (in-order) instruction (one token) from INM and updates the
    # values of the source registers with the values from RGF (with the help of READ transition, as described
    # above), and places the modified instruction token in INB.

    # remove first instruction from INM
    instr = INM_.pop()
    # get the values of the source registers with the values from RGF
    # update the values of the source registers with the values from RGF
    # place the modified instruction token in INB

    # get two values from instr
    src1 = instr.src1
    src2 = instr.src2
    # get the values of the source registers with the values from RGF
    src1_value = RGF_.read(src1)
    src2_value = RGF_.read(src2)

    # update vals
    instr.src1 = src1_value
    instr.src2 = src2_value

    INB_.set_instr(instr)
    global INB_has_token
    INB_has_token = True
    # decode_has_token = False # left up to if theres vals left in INM

def read():
    # knows top down from INM

    # checks for the availability of the source operands in the Register File (RGF) for the top
    return

def ADDR():
    # The ADDR transition performs effective (data memory) address calculation for the load instruction by
    # adding the contents of two source registers. It produces a token as <destination-register-name, data memory
    # address> and places it in the address buffer (ADB).
    global ADB_has_token, ADB_

    ADB_.reg = Register(LIB_.instr.dest, LIB_.instr.src1 + LIB_.instr.src2)
    LIB_.instr = None
    ADB_has_token = True

def load():
    # The LOAD transition consumes a token from ADB and gets the data from the data memory for the
    # corresponding address. Assume that you will always have the data for the respective address in the data
    # memory in the same time step. It places the data value (result of load) in the result buffer (REB). The format
    # of the token in result buffer is same as a token in RGF i.e., <destination-register-name, data value>.
    reg = [ADB_.reg.name, DAM_.read(ADB_.reg.value)]
    reg = Register(reg[0], reg[1])
    ADB_.reg = None
    REB_.registers.append(reg)
    global ADB_has_token
    ADB_has_token = False

def write():
    # The WRITE transition transfers the result (one token) from the Result Buffer (REB) to the register file (RGF).
    # If there are more than one token in REB in a time step, the WRITE transition writes the token that belongs to
    # the in-order first instruction.
    register = REB_.registers.pop(0)
    RGF_.write(register.name, register.value)

    global REB_has_token
    if REB_.is_empty():
        REB_has_token = False
    

def issue1():
    # The ISSUE1 transition consumes one arithmetic/logical (ADD, SUB, AND, OR) instruction token (if any)
    # from INB and places it in the Arithmetic Instruction Buffer (AIB).
    AIB_.instr = INB_.instr
    INB_.instr = None

def issue2():
    # The ISSUE2 transition consumes one load (LD) instruction token (if any) from INB and places it in the Load
    # Instruction Buffer (LIB).
    LIB_.instr = INB_.instr
    INB_.instr = None

def ALU():
    # The ALU transition performs arithmetic/logical computations as per the instruction token from AIB, and
    # places the result in the result buffer (REB). The format of the token in result buffer is same as a token in RGF
    # i.e., <destination-register-name, value>.

    if (AIB_.instr.opcode == 'ADD'):
        REB_.registers.append(Register(AIB_.instr.dest, AIB_.instr.src1 + AIB_.instr.src2))
    elif (AIB_.instr.opcode == 'SUB'):
        REB_.registers.append(Register(AIB_.instr.dest, AIB_.instr.src1 - AIB_.instr.src2))
    elif (AIB_.instr.opcode == 'AND'):
        REB_.registers.append(Register(AIB_.instr.dest, AIB_.instr.src1 & AIB_.instr.src2))
    elif (AIB_.instr.opcode == 'OR'):
        REB_.registers.append(Register(AIB_.instr.dest, AIB_.instr.src1 | AIB_.instr.src2))

    AIB_.instr = None
# for i in instr:
#     print(i)


# 1. READ:
# The READ transition is a slight deviation from traditional Petri net semantics since it does not have any
# direct access to instruction tokens. Assume that it knows the top (in-order) instruction in the Instruction
# Memory (INM). It checks for the availability of the source operands in the Register File (RGF) for the top
# instruction token and passes them to Instruction Buffer (INB) by replacing the source operands with the
# respective values. For example, if the top instruction token in INM is <ADD, R1, R2, R3> and there are two
# tokens in RGF as <R2,5> and <R3,7>, then the instruction token in INB would be <ADD, R1, 5, 7> once
# both READ and DECODE transitions are activated. Both READ and DECODE transitions are executed
# together. Please note that when READ consumes two register tokens, it also returns them to RGF in the same
# time step (no change in RGF due to READ).
# Page 3 of 6
# 2. DECODE:
# The DECODE transition consumes the top (in-order) instruction (one token) from INM and updates the
# values of the source registers with the values from RGF (with the help of READ transition, as described
# above), and places the modified instruction token in INB.
# 3. ISSUE1:
# The ISSUE1 transition consumes one arithmetic/logical (ADD, SUB, AND, OR) instruction token (if any)
# from INB and places it in the Arithmetic Instruction Buffer (AIB).
# 4. ISSUE2:
# The ISSUE2 transition consumes one load (LD) instruction token (if any) from INB and places it in the Load
# Instruction Buffer (LIB).
# 5. Arithmetic Logic Unit (ALU)
# The ALU transition performs arithmetic/logical computations as per the instruction token from AIB, and
# places the result in the result buffer (REB). The format of the token in result buffer is same as a token in RGF
# i.e., <destination-register-name, value>.
# 6. Address Calculation (ADDR)
# The ADDR transition performs effective (data memory) address calculation for the load instruction by
# adding the contents of two source registers. It produces a token as <destination-register-name, data memory
# address> and places it in the address buffer (ADB).
# 7. LOAD:
# The LOAD transition consumes a token from ADB and gets the data from the data memory for the
# corresponding address. Assume that you will always have the data for the respective address in the data
# memory in the same time step. It places the data value (result of load) in the result buffer (REB). The format
# of the token in result buffer is same as a token in RGF i.e., <destination-register-name, data value>.
# 8. WRITE
# The WRITE transition transfers the result (one token) from the Result Buffer (REB) to the register file (RGF).
# If there are more than one token in REB in a time step, the WRITE transition writes the token that belongs to
# the in-order first instruction.
    
    # make one function per transition
    # with notes

# def read_instr():
#     instr = INM.read_instructions()    
#     print(instr)

# read_instr()

write_output()
step += 1

while check_for_tokens():
    # change order to RGF, read, write, load, DAM, ADB, ADDR, LIB, Issue2, ALU, issue1, INB, decode, INM
    # keep blocks of code for each if as written, just change order
    if RGF_has_token:
        # reads at end
        pass
    # if read_has_token:
    #     pass
    if REB_has_token:
        write()
    # if load_has_token:
    #     22pass
    if DAM_has_token:
        pass
    if ADB_has_token:
        load()
        ADB_has_token = False
        REB_has_token = True
    if ADDR_has_token:

        pass
    if LIB_has_token:
        ADDR()
        ADDR_has_token = False
        LIB_has_token = False
    if issue2_has_token:
        issue2_has_token = False
        LIB_has_token = True
    if AIB_has_token:
        ALU()
        AIB_has_token = False
        REB_has_token = True
    if issue1_has_token:
        issue1_has_token = False
        ALU_has_token = True
    if INB_has_token:
        if (INB_.is_instr_arith()):
            INB_has_token = False
            issue1()
            INB_has_token, AIB_has_token = False, True
        else:
            INB_has_token = False
            issue2()
            INB_has_token, LIB_has_token = False, True
    if decode_has_token:
        pass
    if INM_has_token:
        decode()
        INM_has_token = not INM_.is_empty()
        INB_has_token = True
    read() # make sure it gets the right vals

    # write to simulation file
    write_output()
    step += 1


    # if INB_has_token:
    #     if (INB.is_instr_arith()):
    #         INB_has_token = False
    #         issue1_has_token = True
    #     else:
    #         INB_has_token = False
    #         issue2_has_token = True
    # if INM_has_token:
    #     decode()
    #     INM_has_token = not INM.is_empty()
    #     INB_has_token = True
    # if AIB_has_token:
    #     pass
    # if LIB_has_token:
    #     ADDR_var = LIB.instr
    #     LIB_has_token = False
    #     ADDR_has_token = True
    # if ADB_has_token:
    #     pass
    # if REB_has_token:
    #     pass
    # if RGF_has_token:
    #     pass
    # if DAM_has_token:
    #     pass
    # if decode_has_token:
    #     pass
    # if read_has_token:
    #     pass
    # if ADDR_has_token:
    #     ADDR()
    #     pass
    # if load_has_token:
    #     pass
    # if write_has_token:
    #     pass
    # if issue1_has_token:
    #     issue1_has_token = False
    #     ALU_has_token = True
    # if issue2_has_token:
    #     issue2_has_token = False
    #     LIB_has_token = True
    # if ALU_has_token:
    #     ALU()