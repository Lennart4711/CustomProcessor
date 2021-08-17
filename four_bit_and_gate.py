from component import Component
from and_gate import AndGate

class FourBitAndGate(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 4
        super().__init__()
        self.update(input_data)
        

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.output.clear()

        a = AndGate([self.input[0],self.input[1]])
        b = AndGate([self.input[2],self.input[3]])

        out = AndGate(a.output + b.output)
        self.output = out.output


