from dynamic_register import DynamicRegister
from component import Component
from eight_bit_register import EightBitRegister

class RAM(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.update(input_data)
        self.registers = [DynamicRegister(12,[]) for _ in range(256)]
        self.address_memory = EightBitRegister([])

        

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.output.clear()

    def binary_to_decimal(self,binary):
        decimal = 0 
        for digit in binary: 
            decimal = decimal*2 + int(digit) 
        return decimal 

    def array_to_decimal(self,address):
        out = ""
        for i in address:
            if i:
                out += "1"
            else: out += "0"
        return self.binary_to_decimal(out)
    
    def ram_in(self, bus):
        address = self.array_to_decimal(self.address_memory.output)
        self.registers[address].update([True]+[False]*4+bus.output[-8:])

    def ram_out(self, bus):
        address = self.array_to_decimal(self.address_memory.output)
        bus.output = self.registers[address].output.copy()
    
    
    def address_in(self, bus):
        self.address_memory.update([True]+bus.output)
