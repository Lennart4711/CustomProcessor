from component import Component
from four_bit_adder import FourBitAdder
from xor_gate import XorGate
from not_gate import NotGate
from and_gate import AndGate


class Alu(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 9
        super().__init__()
        self.update(input_data)

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic--------#
        self.output.clear()
        self.xor_one = XorGate([self.input[4], self.input[8]])
        self.xor_two = XorGate([self.input[5], self.input[8]])
        self.xor_three = XorGate([self.input[6], self.input[8]])
        self.xor_four = XorGate([self.input[7], self.input[8]])
        self.adder = FourBitAdder([self.input[0],self.input[1],self.input[2],self.input[3],self.xor_one.output[0],self.xor_two.output[0],self.xor_three.output[0],self.xor_four.output[0]])
        self.not_one = NotGate([self.adder.output[0]])
        self.not_two = NotGate([self.adder.output[1]])
        self.not_three = NotGate([self.adder.output[2]])
        self.not_four = NotGate([self.adder.output[3]])
        self.and_one = AndGate([self.not_one.output[0],self.not_two.output[0]])
        self.and_two = AndGate([self.and_one.output[0],self.not_three.output[0]])
        self.and_three = AndGate([self.and_two.output[0], self.not_four.output[0]])
        self.output = [self.adder.output[3],self.adder.output[2],self.adder.output[1],self.adder.output[0]]

