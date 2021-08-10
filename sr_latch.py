import random
from component import Component
from not_gate import NotGate
from or_gate import OrGate
from and_gate import AndGate
        

class SrLatch(Component):
    def __init__(self,input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        
        self.not_gate = NotGate([False])
        self.or_gate = OrGate([False,False])
        self.and_gate = AndGate([self.or_gate.output, self.not_gate.output])
        self.output = self.and_gate.output
        self.update(input_data)
    

    #First is set, second is reset
    def update(self,input_data):
        self.clear_input(input_data)
        #-----------Logic-------------#
        
        #self.metastable()
        self.not_gate.update([self.input[1]])
        self.or_gate.update([self.and_gate.output[0],self.input[0]])
        self.and_gate.update([self.or_gate.output[0],self.not_gate.output[0]])
        self.or_gate.update([self.and_gate.output[0],self.input[0]])
        self.output = self.and_gate.output

    #pobably not nescry cuase d latch doesnt allow 1,1 as input to set/reset
    #metastability accurs in hardware when there is a "racing condition" in  the loop
    def metastable(self):
        if(all(self.input)):
            if(bool(random.getrandbits(1))):
                self.input[1] = False
            else:
                self.input[0] = False