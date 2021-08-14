from component import Component
from adder import Adder


class DynamicAdder(Component):
    def __init__(self, bits, input_data):
        self.INPUT_LENGTH = bits * 2 + 1
        self.bits = bits
        super().__init__()
        
        self.adders = []
        for _ in range(bits):
            self.adders.append(Adder([False,False,False]))
        self.update(input_data)


    def update(self, input_data):
        self.clear_input(input_data)


        #-----------Logic--------#
        self.output.clear()

        self.adders[0].update([self.input[self.bits-1],self.input[self.bits*2-1],self.input[self.bits*2]])
        self.output.append(self.adders[0].output[0])

        for i in range(1,self.bits):
            
            self.adders[i].update([self.input[self.bits-1-i],self.input[self.bits*2-1-i],self.adders[i-1].output[1]])
            self.output.append(self.adders[i].output[0])

        self.output.reverse()
        self.output.append(self.adders[self.bits-1].output[1])
        




