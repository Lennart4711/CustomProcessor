from dynamic_register import DynamicRegister
from component import Component

class FourBitRegister(Component):
    def __init__(self, input_data):
        super().__init__()
        self.INPUT_LENGTH = 5
        self.register = DynamicRegister(4,input_data)
        self.output = self.register.output

    
    def update(self, input_data):
        self.clear_input(input_data)
        #-----------Logic-------------#
        self.register.update(self.input)
        self.output = self.register.output

    