from xor_gate import XorGate
from not_gate import NotGate
from component import Component

class XnorGate(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.update(input_data)
    
    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.output.clear()

        xor_gate = XorGate(self.input)
        not_gate = NotGate(xor_gate.output)
        self.output = not_gate.output