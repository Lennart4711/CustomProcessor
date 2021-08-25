from dynamic_register import DynamicRegister
from component import Component
from eight_bit_register import EightBitRegister
from helper import *

class RAM(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.registers = [DynamicRegister(12,[]) for _ in range(256)]
        #memory address register
        self.address_memory = EightBitRegister([])
    
    def address_in(self, bus):
            self.address_memory.update([True]+bus.output)

    def ram_in(self, bus):
        address = array_to_decimal(self.address_memory.output)
        #store, instruction bits, data
        self.registers[address].update([True]+[False]*4+bus.output)

    def ram_out(self, bus):
        address = array_to_decimal(self.address_memory.output)
        bus.output = self.registers[address].output.copy()
    
    
    