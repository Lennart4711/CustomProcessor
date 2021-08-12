from component import Component
from adder import Adder


class FourBitAdder(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 9
        super().__init__()
        self.update(input_data)

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic--------#
        self.output.clear()

        self.adder_one = Adder([self.input[3],self.input[7], self.input[8]])
        self.adder_two = Adder([self.input[2],self.input[6], self.adder_one.output[1]])
        self.adder_three = Adder([self.input[1],self.input[5], self.adder_two.output[1]])
        self.adder_four = Adder([self.input[0],self.input[4], self.adder_three.output[1]])
        self.output = [self.adder_one.output[0],self.adder_two.output[0],self.adder_three.output[0],self.adder_four.output[0], self.adder_four.output[1]]


        