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
        print("NOP")
    elif(x == 1):
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        ram.ram_out(bus)
        a_register.register_in(bus)
        print("LDA", a_register.output)

    elif(x == 2):
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        ram.ram_out(bus)
        b_register.register_in(bus)
        print("LDB", b_register.output)
        alu.sum_out(bus, a_register,b_register,[False])
        a_register.register_in(bus)
        print("ADD", a_register.output)
    elif(x == 3):
        print("SUB")
    elif(x == 4):
        print("STA")
    elif(x == 5):
        print("LDI")
    elif(x == 6):
        print("JMP")
    elif(x == 7):
        print("JC") 
    elif(x == 8):
        print("JZ")       
    elif(x == 14):
        print("OUT")
    elif(x == 15):
        print("HLT")
    

    
if __name__ == "__main__":
    #--------components---------#
    bus = Bus(8,[])
    bus.update(parse_bits("11111111"))

    pc = ProgramCounter()

    ram = RAM([])
    ram.registers[0].update(parse_bits("1 0001 11111110"))
    ram.registers[1].update(parse_bits("1 0010 11111111"))
    ram.registers[254].update(parse_bits("1 0001 00000101"))
    ram.registers[255].update(parse_bits("1 0010 00000001"))
    
    
    instructions_register = DynamicRegister(12,[])

    alu = Alu(8,[])

    a_register = DynamicRegister(8, parse_bits("1 00000000"))
    b_register = DynamicRegister(8, parse_bits("1 00000000"))

    for i in ram.registers:
        print(i.output)

    #fetch instructions from memory
    for i in range(2):
        pc.counter_out(bus)
        ram.address_in(bus)
        ram.ram_out(bus)
        instructions_register.update([True]+bus.output)
        pc.count_enable()
        
        next_instruction(array_to_decimal(instructions_register.output[:4]))

    
    
