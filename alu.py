from dynamic_adder import DynamicAdder
from component import Component
from four_bit_adder import FourBitAdder
from xor_gate import XorGate
from not_gate import NotGate
from and_gate import AndGate


class Alu(Component):
    #last is subtract signal, 
    #first n is first number, 
    #second n is second number (n is equal to bits)
    def __init__(self,bits, input_data):
        super().__init__()
        self.bits = bits
        self.INPUT_LENGTH = bits*2+1
        self.update(input_data)

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic--------#
        self.output.clear()
        self.xor_gates = []
        for i in range(self.bits):
            self.xor_gates.append(XorGate([self.input[self.bits+i],self.input[self.bits*2]]))
        

        xor_out = []
        for gate in self.xor_gates:
            xor_out.append(gate.output[0])

        self.adder = DynamicAdder(self.bits,self.input[:self.bits]+xor_out+[self.input[self.bits]])
        self.output = self.adder.output