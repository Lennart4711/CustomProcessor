from not_gate import NotGate
from and_gate import AndGate
from component import Component


class NandGate(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.update(input_data)



    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        and_gate = AndGate(self.input)
        inverter = NotGate(and_gate.output)
        self.output = inverter.output
