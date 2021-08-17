from dynamic_adder import DynamicAdder
from component import Component

class FourBitAdder(Component):
    def __init__(self, input_data):
        super().__init__()
        self.INPUT_LENGTH = 9
        self.adder = DynamicAdder(4,input_data)
        self.output = self.adder.output

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic--------#
        self.output.clear()
        self.adder.update(input_data)
        self.output = self.adder.output
