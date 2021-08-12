from component import Component
from adder import Adder


class EightBitAdder(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 17
        super().__init__()
        self.update(input_data)

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic--------#
        self.output.clear()

        self.adder_one = Adder([self.input[7],self.input[15], self.input[16]])
        self.adder_two = Adder([self.input[6],self.input[14], self.adder_one.output[1]])
        self.adder_three = Adder([self.input[5],self.input[13], self.adder_two.output[1]])
        self.adder_four = Adder([self.input[4],self.input[12], self.adder_three.output[1]])
        self.adder_five = Adder([self.input[3],self.input[11], self.adder_four.output[1]])
        self.adder_six = Adder([self.input[2],self.input[10], self.adder_five.output[1]])
        self.adder_seven = Adder([self.input[1],self.input[9], self.adder_six.output[1]])
        self.adder_eight = Adder([self.input[0],self.input[8], self.adder_seven.output[1]])
        self.output = [self.adder_one.output[0],self.adder_two.output[0],self.adder_three.output[0],self.adder_four.output[0],self.adder_five.output[0],self.adder_six.output[0], self.adder_seven.output[0], self.adder_eight.output[0], self.adder_eight.output[1]]

        #TODO: build dynamic adder, because building it like this is trash


        