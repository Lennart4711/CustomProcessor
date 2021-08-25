from not_gate import NotGate
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
        not_left = NotGate([self.input[0]])
        not_right = NotGate([self.input[1]])

        nand_exit = NandGate([not_right.output[0], not_left.output[0]])
        self.output = nand_exit.output
