from component import Component
from data_latch import DataLatch

class FourBitRegister(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 5
        super().__init__()
        self.output = [False]*4
        self.update(input_data)

    
    def update(self, input_data):
        self.clear_input(input_data)
        #-----------Logic-------------#
        self.reg_one = DataLatch([self.input[0], self.input[4]])
        self.reg_two = DataLatch([self.input[1], self.input[4]])
        self.reg_three = DataLatch([self.input[2], self.input[4]])
        self.reg_four = DataLatch([self.input[3], self.input[4]])
        self.output = [self.reg_one.output[0], self.reg_two.output[0], self.reg_three.output[0], self.reg_four.output[0]]
