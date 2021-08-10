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

if __name__ == "__main__":
    d = Adder([True,False,True])
    print(d.output)
    d.update([True,True,True])
    print(d.output)
