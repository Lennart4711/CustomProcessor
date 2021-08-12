from alu import Alu
from eight_bit_adder import EightBitAdder
from four_bit_adder import FourBitAdder
from adder import Adder
from dynamic_register import DynamicRegister
from eight_bit_register import EightBitRegister
from data_latch import DataLatch
from sr_latch import SrLatch
from xor_gate import XorGate
from or_gate import OrGate
from nand_gate import NandGate
from buffer import Buffer
from not_gate import NotGate
from and_gate import AndGate
from nor_gate import NorGate
from xnor_gate import XnorGate
from four_bit_register import FourBitRegister

def stringToArray(string):
    bits = []
    for char in string:
        if char == '1':
            bits.append(True)
        elif char == '0':
            bits.append(False)
        else: 
            print("This is not a quantum computer")
    return bits

if __name__ == "__main__":
    d = Alu(stringToArray("0111 0011 0"))
    print(d.output)

#TODO: norm the direction of output in register, adder and alu
