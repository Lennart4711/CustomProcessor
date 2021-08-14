from dynamic_adder import DynamicAdder
from component import Component


class EightBitAdder(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 17
        super().__init__()
        self.adder = DynamicAdder(8,input_data)
        self.output = self.adder.output

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic--------#
        self.output.clear()
        self.adder.update(input_data)
        self.output = self.adder.output



        