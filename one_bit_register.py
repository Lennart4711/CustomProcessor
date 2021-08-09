from or_gate import OrGate
from not_gate import NotGate
from and_gate import AndGate
from component import Component
from data_latch import DataLatch


#First is Data, second is store, third is clock
class OneBitRegister(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 3
        super().__init__()  
        self.data_latch = DataLatch([False,True])
        self.update(input_data)
        

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.not_gate = NotGate([self.input[1]])
        self.and_store = AndGate([self.input[1],self.input[0]])
        self.and_keep = AndGate([self.data_latch.output[0],self.not_gate.output[0]])
        self.or_gate = OrGate([self.and_keep.output[0],self.and_store.output[0]])
        self.data_latch.update([self.or_gate.output[0],self.input[2]])
        self.output = self.data_latch.output