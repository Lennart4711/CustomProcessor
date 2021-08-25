from not_gate import NotGate
from and_gate import AndGate
from component import Component
from sr_latch import SrLatch

class DataLatch(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.sr_latch = SrLatch([])
        self.update(input_data)

    #First is data,second is store
    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.not_gate = NotGate([self.input[0]])
        self.and_set = AndGate([self.input[0],self.input[1]])
        self.and_reset = AndGate([self.input[1], self.not_gate.output[0]])
        self.sr_latch.update([self.and_set.output[0],self.and_reset.output[0]])
        self.output = self.sr_latch.output
