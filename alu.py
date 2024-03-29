from data_latch import DataLatch
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
    def __init__(self,bits):
        super().__init__()
        self.bits = bits
        self.INPUT_LENGTH = bits*2+1

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic--------#
        #subtract signal
        self.xor_gates = [
            XorGate([self.input[self.bits + i], self.input[self.bits * 2]])
            for i in range(self.bits)
        ]

        xor_out = [gate.output[0] for gate in self.xor_gates]
        #first half, second half through xor_gates, carry bit
        self.adder = DynamicAdder(self.bits,self.input[:self.bits]+xor_out+[self.input[self.bits*2]])
        self.output = self.adder.output[:-1]

        self.carry_flag = self.adder.output[8]
        self.zero_flag = not any(self.adder.output[:-1])
        


    def sum_out(self,bus,reg_a, reg_b,carry):
        self.update(reg_a.output+reg_b.output+carry)
        bus.update(self.output)

            