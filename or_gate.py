from nand_gate import NandGate
from component import Component

class OrGate(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.update(input_data)

    
    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.output.clear()
        nand_left = NandGate([self.input[0],self.input[0]])
        nand_right = NandGate([self.input[1],self.input[1]])

        nand_exit = NandGate([nand_right.output[0], nand_left.output[0]])
        self.output = nand_exit.output
