from component import Component

class NotGate(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 1
        super().__init__()
        self.update(input_data)

    def update(self, input_data):
        self.clear_input(input_data)
        
        #-----------Logic--------#
        self.output = [not self.input[0]]