from component import Component
from data_latch import DataLatch

class DynamicRegister(Component):
    #input at [0] is wether to store or not
    def __init__(self, length,input_data):
        self.INPUT_LENGTH = length+1
        super().__init__()
        self.update(input_data)

    
    def update(self, input_data):
        self.clear_input(input_data)
        #-----------Logic-------------#
        self.registers = []
        self.output = []
        for i in range(self.INPUT_LENGTH-1):
            self.registers.append(DataLatch([self.input[i+1],self.input[0]]))
            self.output.append(self.registers[i].output[0])

    def register_out(self, bus):
        bus.update(self.output)
    
    def register_in(self, bus):
        self.update([True]+bus.output)