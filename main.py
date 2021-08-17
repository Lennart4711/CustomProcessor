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

if __name__ == "__main__":

    architecture = 8 #bits
    bus = Bus(architecture,[])
    a_register = DynamicRegister(architecture, parse_bits("1 00000101"))
    b_register = DynamicRegister(architecture, parse_bits("1 00000001"))
    print("rega:",a_register.output)
    print("regb:",b_register.output)

    alu = Alu(architecture, a_register.output+b_register.output+[False])
    alu.sum_out(bus, a_register,b_register,[False])

    print(bus.output)
  

    
