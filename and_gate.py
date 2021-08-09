from component import Component


class AndGate(Component):
    def __init__(self, input_data):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.update(input_data)
        

    def update(self, input_data):
        self.clear_input(input_data)

        #-----------Logic-------------#
        self.output.clear()
        if all(self.input):
            self.output.append(True)
        else: self.output.append(False)

