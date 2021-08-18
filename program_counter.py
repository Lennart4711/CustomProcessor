from component import Component
from eight_bit_register import EightBitRegister
from eight_bit_adder import EightBitAdder

class ProgramCounter(Component):
    def __init__(self):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.adder = EightBitAdder([])
        self.register = EightBitRegister([])
        self.update()
        

    def update(self):

        #-----------Logic-------------#
        self.output.clear()

    def counter_out(self, bus):
        bus.update(self.register.output)

    def count_enable(self):
        self.adder.update(self.register.output+[False,False,False,False,False,False,False,True])
        self.register.update([True]+self.adder.output)

    def jump(self, address):
        self.register.update([True]+address)
