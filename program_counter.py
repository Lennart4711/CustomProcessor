from component import Component
from eight_bit_register import EightBitRegister
from eight_bit_adder import EightBitAdder

class ProgramCounter(Component):
    def __init__(self):
        self.INPUT_LENGTH = 2
        super().__init__()
        self.adder = EightBitAdder()
        self.counter = EightBitRegister([])

    def counter_out(self, bus):
        bus.update(self.counter.output)

    def count_enable(self):
        self.adder.update(self.counter.output+[False]*7+[True])
        self.counter.update([True]+self.adder.output)

    def jump(self, bus):
        self.counter.update([True]+bus.output)
