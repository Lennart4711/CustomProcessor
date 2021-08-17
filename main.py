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
        return decimal -1

def array_to_decimal(self,address):
        out = ""
        for i in address:
            if i:
                out += "1"
            else: out += "0"
        return self.binary_to_decimal(out)


if __name__ == "__main__":

    architecture = 8 #bits

    bus = Bus(architecture,[])
    bus.update(parse_bits("11111111"))

    pc = ProgramCounter()
    pc.jump(parse_bits("11011011"))
    pc.counter_out(bus)
    
    print(bus.output)
















    #a_register = DynamicRegister(architecture, parse_bits("1 00000101"))
    #b_register = DynamicRegister(architecture, parse_bits("1 00000001"))
    #print("rega:",a_register.output)
    #print("regb:",b_register.output)

    #alu = Alu(architecture, a_register.output+b_register.output+[False])
    #alu.sum_out(bus, a_register,b_register,[False])

    """


    ram = RAM([])
    print("bus:",bus.output)
    ram.address_in(bus)
    bus.update(parse_bits("00000001"))
    ram.ram_in(bus)
    ram.ram_out(bus)
    print("bus:",bus.output)
    print(ram.registers[254].output)"""


    
