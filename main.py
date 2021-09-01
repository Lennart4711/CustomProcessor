from program_counter import ProgramCounter
from ram import RAM
from adder import Adder
from alu import Alu
from and_gate import AndGate
from buffer import Buffer
from data_latch import DataLatch
from dynamic_adder import DynamicAdder
from dynamic_register import DynamicRegister
from eight_bit_adder import EightBitAdder
from eight_bit_register import EightBitRegister
from four_bit_adder import FourBitAdder
from four_bit_and_gate import FourBitAndGate
from four_bit_register import FourBitRegister
from nand_gate import NandGate
from nor_gate import NorGate
from not_gate import NotGate
from or_gate import OrGate
from sr_latch import SrLatch
from xnor_gate import XnorGate
from xor_gate import XorGate
from bus import Bus
from helper import *




def next_instruction(x):
    if(x == 0):
        #NOP
        pass
    elif(x == 1):
        #LDA
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        ram.ram_out(bus)
        a_register.register_in(bus)
    elif(x == 2):
        #ADD
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        ram.ram_out(bus)
        b_register.register_in(bus)
        alu.sum_out(bus, a_register,b_register,[False])
        a_register.register_in(bus)
    elif(x == 3):
        #SUB
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        ram.ram_out(bus)
        b_register.register_in(bus)
        alu.sum_out(bus, a_register,b_register,[True])
        a_register.register_in(bus)
    elif(x == 4):
        #STA
        bus.update(instructions_register.output[4:])
        ram.address_in(bus)
        a_register.register_out(bus)
        ram.ram_in(bus)

    elif(x == 5):
        #LDI
        bus.update(instructions_register.output[4:])
        a_register.register_in(bus)
    elif(x == 6):
        #JMP
        bus.update(instructions_register.output[4:])
        pc.jump(bus)
    elif(x == 7):
        #JC
        if(alu.carry_flag):
            bus.update(instructions_register.output[4:])
            pc.jump(bus)
    elif(x == 8):
        #JZ
        if(alu.zero_flag):
            bus.update(instructions_register.output[4:])
            pc.jump(bus)#
    elif(x == 14):
        #OUT
        print(a_register.output)
    elif(x == 15):
        #HLT
        exit()
        
def count_up(ram):
    #this program adds 1 to value at 255 and stores it back in there
    #Then it checks if the number doesnt fit in 8bits
    #If that is the case, it halts
    #Else it adds 1 again
    ram.registers[0].update(parse_bits("1 0001 11111111"))#LDA 255
    ram.registers[1].update(parse_bits("1 0010 11111110"))#ADD 254
    ram.registers[2].update(parse_bits("1 1110 00000000"))#OUT A-Registers
    ram.registers[3].update(parse_bits("1 0100 11111111"))#STA 255
    ram.registers[4].update(parse_bits("1 0111 00000110"))#JMC 6
    ram.registers[5].update(parse_bits("1 0110 00000000"))#JMP 0
    ram.registers[6].update(parse_bits("1 1111 00000000"))#HLT 0
    
    ram.registers[254].update(parse_bits("1 0000 00000001"))
    ram.registers[255].update(parse_bits("1 0000 00000000"))

def multiply(ram):
    ram.registers[0].update(parse_bits("1 0001 11111111"))#lda f2
    ram.registers[1].update(parse_bits("1 0100 11111101"))#sta turn
    ram.registers[3].update(parse_bits("1 0011 11111011"))#sub one
    ram.registers[4].update(parse_bits("1 1000 00001100"))#jz hlt
    ram.registers[5].update(parse_bits("1 0001 11111100"))#lda out
    ram.registers[6].update(parse_bits("1 0010 11111110"))#add f1
    ram.registers[7].update(parse_bits("1 0100 11111100"))#sta out
    ram.registers[8].update(parse_bits("1 0001 11111101"))#lda turn
    ram.registers[9].update(parse_bits("1 0011 11111011"))#sub one
    ram.registers[10].update(parse_bits("1 0100 11111101"))#sta turn
    ram.registers[11].update(parse_bits("1 0110 00000010"))#j 
    ram.registers[12].update(parse_bits("1 0001 11111100"))#lda out
    ram.registers[13].update(parse_bits("1 1110 00000000"))#out
    ram.registers[14].update(parse_bits("1 1111 00000000"))#hlt

    ram.registers[250].update(parse_bits("1 0000 00000001"))#zero
    ram.registers[251].update(parse_bits("1 0000 00000001"))#one
    ram.registers[252].update(parse_bits("1 0000 00000000"))#out
    ram.registers[253].update(parse_bits("1 0000 00000000"))#turn
    ram.registers[254].update(parse_bits("1 0000 11111111"))#F1
    ram.registers[255].update(parse_bits("1 0000 00000101"))#F2 #enter one more
    
def halt_if_zero(ram):
    ram.registers[0].update(parse_bits("1 0001 11111111"))#lda 1
    ram.registers[1].update(parse_bits("1 0011 11111110"))#sub 1
    ram.registers[2].update(parse_bits("1 1000 00000001"))#jz hlt
    ram.registers[3].update(parse_bits("1 0110 00000000"))#one
    ram.registers[4].update(parse_bits("1 1111 00000000"))#one

    ram.registers[254].update(parse_bits("1 0000 00000001"))#F1
    ram.registers[255].update(parse_bits("1 0000 00000001"))#F2

    
if __name__ == "__main__":
    #--------components---------#
    bus = Bus(8,[])

    pc = ProgramCounter()

    ram = RAM([])
    multiply(ram)
    #halt_if_zero(ram)
    
    instructions_register = DynamicRegister(12,[])

    alu = Alu(8,[])

    a_register = DynamicRegister(8, parse_bits("1 00000000"))
    b_register = DynamicRegister(8, parse_bits("1 00000000"))


    
    while True:
        #fetch instructions from memory
        pc.counter_out(bus)
        ram.address_in(bus)
        ram.ram_out(bus)
        instructions_register.update([True]+bus.output)
        pc.count_enable()
        #microinstruction
        next_instruction(array_to_decimal(instructions_register.output[:4]))

#Unoptimized code takes 3.6 seconds
