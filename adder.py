from or_gate import OrGate
from and_gate import AndGate
from xor_gate import XorGate
from component import Component


class Adder(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 3
        super().__init__()
        self.update(input_data)

    def update(self, input_data):
        self.clear_input(input_data)

        #input: 0 = first bit, 1 = second bit, 2 = carry bit
        #-----------Logic--------#
        self.xor_one = XorGate([self.input[0],self.input[1]])
        self.and_one = AndGate([self.input[0],self.input[1]])
        self.xor_two= XorGate([self.xor_one.output[0],self.input[2]])
        self.and_two = AndGate([self.input[2], self.xor_one.output[0]])
        self.or_gate = OrGate([self.and_one.output[0], self.and_two.output[0]])
        #solution, carry
        self.output = [self.xor_two.output[0],self.or_gate.output[0]]