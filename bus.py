from component import Component

class Bus(Component):
    def __init__(self, architecture,input_data):
        self.INPUT_LENGTH = architecture
        super().__init__()
        self.update(input_data)
        

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.output.clear()
        self.output = self.input


