from program_counter import ProgramCounter
from ram import RAM
from adder import Adder
from alu import Alu
from and_gate import AndGate
from buffer import Buffer
from data_latch import DataLatch
from dynamic_adder import DynamicAdder
from dynamic_register import DynamicRegister
from eight_bit_adder import EightBitAdder
from eight_bit_register import EightBitRegister
from four_bit_adder import FourBitAdder
from four_bit_and_gate import FourBitAndGate
from four_bit_register import FourBitRegister
from nand_gate import NandGate
from nor_gate import NorGate
from not_gate import NotGate
from or_gate import OrGate
from sr_latch import SrLatch
from xnor_gate import XnorGate
from xor_gate import XorGate
from bus import Bus
import time


def parse_bits(string):
    bits = []
    for char in string:
        if char == '1':
            bits.append(True)
        elif char == '0':
            bits.append(False)
        else:
            pass 
            #print("This is not a quantum computer")
    return bits

def binary_to_decimal(binary):
        decimal = 0 
        for digit in binary: 
            decimal = decimal*2 + int(digit) 
        return decimal 

def array_to_decimal(address):
        out = ""
        for i in address:
            if i:
                out += "1"
            else: out += "0"
        return binary_to_decimal(out)

def next_instruction(x):
    if(x == 0):
        #NOP
        pass
    elif(x == 1):
        #LDA
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        ram.ram_out(bus)
        a_register.register_in(bus)
    elif(x == 2):
        #ADD
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        ram.ram_out(bus)
        b_register.register_in(bus)
        alu.sum_out(bus, a_register,b_register,[False])
        a_register.register_in(bus)
    elif(x == 3):
        #SUB
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        ram.ram_out(bus)
        b_register.register_in(bus)
        alu.sum_out(bus, a_register,b_register,[True])
        a_register.register_in(bus)
    elif(x == 4):
        #STA
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        a_register.register_out(bus)
        ram.ram_in(bus)
    elif(x == 5):
        #LDI
        bus.update(instructions_register.output[4:])
        a_register.register_in(bus)
    elif(x == 6):
        #JMP
        bus.update(instructions_register.output[4:])
        pc.jump(bus.output)
    elif(x == 7):
        #JC
        if(alu.carry_flag):
            bus.update(instructions_register.output[4:])
            pc.jump(bus.output)
    elif(x == 8):
        #JZ
        if(alu.zero_flag):
            bus.update(instructions_register.output[4:])
            pc.jump(bus.output)
    elif(x == 14):
        #OUT
        print(a_register.output)
    elif(x == 15):
        #HLT
        print(time.process_time() - start)
        exit()
        

    
if __name__ == "__main__":
    #--------components---------#
    start = time.process_time()
    bus = Bus(8,[])
    bus.update(parse_bits("11111111"))

    pc = ProgramCounter()

    ram = RAM([])
    #this program adds 1 to value at 255 and stores it back in there
    #Then it checks if the number doesnt fit in 8bits
    #If that is the case, it halts
    #Else it adds 1 again
    ram.registers[0].update(parse_bits("1 0001 11111111"))#LDA 255
    ram.registers[1].update(parse_bits("1 0010 11111110"))#ADD 254
    ram.registers[2].update(parse_bits("1 1110 00000000"))#OUT A-Registers
    ram.registers[3].update(parse_bits("1 0100 11111111"))#STA 255
    ram.registers[4].update(parse_bits("1 0111 00000110"))#JMC 6
    ram.registers[5].update(parse_bits("1 0110 00000000"))#JMP 0
    ram.registers[6].update(parse_bits("1 1111 00000000"))#HLT 0
    

    ram.registers[254].update(parse_bits("1 0000 00000001"))
    ram.registers[255].update(parse_bits("1 0000 00000000"))
    
    instructions_register = DynamicRegister(12,[])

    alu = Alu(8,[])

    a_register = DynamicRegister(8, parse_bits("1 00000000"))
    b_register = DynamicRegister(8, parse_bits("1 00000000"))

    
    while True:
        #fetch instructions from memory
        pc.counter_out(bus)
        ram.address_in(bus)
        ram.ram_out(bus)
        instructions_register.update([True]+bus.output)
        pc.count_enable()
        #microinstruction
        next_instruction(array_to_decimal(instructions_register.output[:4]))


#Unoptimized code takes 3.6 seconds