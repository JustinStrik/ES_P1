import INM
import RGF
import DAM
import INB
import AIB
import LIB
import ADB
import REB
from register import Register

INM_has_token, INB_has_token, AIB_has_token, LIB_has_token, ADB_has_token, REB_has_token, RGF_has_token, DAM_has_token = True, False, False, False, False, False, False, False
decode_has_token, read_has_token, ADDR_has_token, load_has_token, write_has_token, issue1_has_token, issue2_has_token, ALU_has_token = False, False, False, False, False, False, False, False

INM_ = INM.INM()
RGF_ = RGF.RGF()
DAM_ = DAM.DAM()
INB_ = INB.INB()
AIB_ = AIB.AIB()
LIB_ = LIB.LIB()
ADB_ = ADB.ADB()
REB_ = REB.REB()

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
    ADB_has_token = False

def write():
    # The WRITE transition transfers the result (one token) from the Result Buffer (REB) to the register file (RGF).
    # If there are more than one token in REB in a time step, the WRITE transition writes the token that belongs to
    # the in-order first instruction.
    while (len(REB_.registers) > 0):
        # register is name r[0-7], get the number
        register = REB_.registers.pop()
        RGF_.write(register.name, register.value)
    pass

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