from and_gate import AndGate
from nand_gate import NandGate
from or_gate import OrGate
from component import Component

class XorGate(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.update(input_data)
    
    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.output.clear()

        nand_gate = NandGate([self.input[0],self.input[1]])
        or_gate = OrGate([self.input[0],self.input[1]])
        and_gate = AndGate([nand_gate.output[0],or_gate.output[0]])
        self.output = and_gate.output