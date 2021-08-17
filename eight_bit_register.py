from dynamic_register import DynamicRegister
from component import Component

class EightBitRegister(Component):
    def __init__(self, input_data):
        super().__init__()
        self.INPUT_LENGTH = 9
        self.register = DynamicRegister(8,input_data)
        self.output = self.register.output

    
    def update(self, input_data):
        self.clear_input(input_data)
        #-----------Logic-------------#
        self.register.update(input_data)
        self.output = self.register.output

    def register_out(self, bus):
        bus.update(self.output)
    
    def register_in(self, bus):
        self.update([True]+bus.output)
