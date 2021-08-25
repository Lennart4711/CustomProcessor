from dynamic_adder import DynamicAdder
from component import Component


class EightBitAdder(Component):
    def __init__(self):
        self.INPUT_LENGTH = 17
        super().__init__()
        self.adder = DynamicAdder(8,[])
        

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic--------#
        self.adder.update(input_data)
        self.output = self.adder.output



        