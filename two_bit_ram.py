from and_gate import AndGate
from component import Component
from not_gate import NotGate
from dynamic_register import DynamicRegister

class FourBitRam(Component):
    def __init__(self, bits, input_data):
        self.INPUT_LENGTH = 2
        #the bits is the size of the register 
        self.bits = bits
        super().__init__()
        self.update(input_data)
        

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.output.clear()
        self.not_0 = NotGate(self.input[0])
        self.not_1 = NotGate(self.input[1])

        self.and_0 = AndGate([self.not_0.output,self.not_1.output])
        self.and_1 = AndGate([self.not_0.output,self.not_1.output])
        self.and_2 = AndGate([self.not_0.output,self.not_1.output])
        self.and_3 = AndGate([self.not_0.output,self.not_1.output])

        self.reg_0 = DynamicRegister(self.bits, self.and_0.output)
        self.reg_1 = DynamicRegister(self.bits, self.and_1.output)
        self.reg_2 = DynamicRegister(self.bits, self.and_2.output)
        self.reg_3 = DynamicRegister(self.bits, self.and_3.output)
