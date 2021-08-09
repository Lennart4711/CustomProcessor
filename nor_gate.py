from not_gate import NotGate
from or_gate import OrGate
from component import Component

class NorGate(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.update(input_data)
    
    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.output.clear()
        or_gate = OrGate(self.input)
        not_gate = NotGate(or_gate.output)
        self.output = not_gate.output