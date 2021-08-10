from component import Component
from data_latch import DataLatch

class DynamicRegister(Component):
    def __init__(self, length,input_data):
        self.INPUT_LENGTH = length+1
        super().__init__()
        self.output = [False]*length
        self.update(input_data)

    
    def update(self, input_data):
        self.clear_input(input_data)
        #-----------Logic-------------#
        self.registers = []
        self.output = []
        for i in range(self.INPUT_LENGTH-1):
            self.registers.append(DataLatch([self.input[i+1],self.input[0]]))
            self.output.append(self.registers[i].output[0])