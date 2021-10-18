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
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()


def next_instruction(x):
    if(x == 0):
        #NOP
        pass
    elif(x == 1):
        #LDA
        print("LDA")
        bus.update(instructions_register.output[4:])
        draw_bus()
        ram.address_in(bus)
        draw_ram()
        print("     IO MI")
        tick()

        ram.ram_out(bus)
        draw_ram(True)
        draw_bus()
        a_register.register_in(bus)
        draw_a_register()
        alu.update(a_register.output+b_register.output+[False])
        draw_alu()
        print("     RO AI")
        tick()

    elif(x == 2):
        print("ADD")
        #ADD
        bus.update(instructions_register.output[4:])
        draw_bus()
        ram.address_in(bus)
        draw_ram()
        print("     IO MI")
        tick()
        
        ram.ram_out(bus)
        draw_bus()
        draw_ram(True)
        b_register.register_in(bus)
        draw_b_register()
        print("     RO BI")
        tick()
        draw_ram()

        alu.sum_out(bus, a_register,b_register,[False])
        draw_bus()
        draw_alu(True)
        a_register.register_in(bus)
        draw_a_register()
        #alu.update(a_register.output+b_register.output+[False])
        print("     AO AI")
        tick()
        draw_alu()


    elif(x == 3):
        #SUB
        print("SUB")
        bus.update(instructions_register.output[4:])
        draw_bus()
        ram.address_in(bus)
        draw_ram()
        print("     IO MI")
        tick()
        
        ram.ram_out(bus)
        draw_bus()
        draw_ram(True)
        b_register.register_in(bus)
        draw_b_register()
        print("     RO BI")
        tick()
        draw_ram()

        alu.sum_out(bus, a_register,b_register,[True])
        draw_bus()
        draw_alu(True)
        a_register.register_in(bus)
        draw_a_register()
        #alu.update(a_register.output+b_register.output+[False])
        print("     AO AI")
        tick()
        draw_alu()
        
    elif(x == 4):
        #STA
        print("STA")
        bus.update(instructions_register.output[4:])
        draw_bus()
        ram.address_in(bus)
        draw_ram()
        print("     IO RI")
        tick()

        a_register.register_out(bus)
        #draw a with out signal
        ram.ram_in(bus)
        draw_ram()
        print("     AO RI")

    elif(x == 5):
        #LDI
        print("LDI")
        bus.update(instructions_register.output[4:])
        draw_bus()
        a_register.register_in(bus)
        draw_a_register()
        print("     IO AI")
        tick()

    elif(x == 6):
        #J
        print("J")
        bus.update(instructions_register.output[4:])
        draw_bus()
        pc.jump(bus)
        draw_program_counter()
        print("     IO J")
    elif(x == 7):
        #JC
        print("JC")
        if(alu.carry_flag):
            bus.update(instructions_register.output[4:])
            draw_bus()
            pc.jump(bus)
            draw_program_counter()
            print("     IO J")
        else: print("     NC")
        tick()
    elif(x == 8):
        #JZ
        print("JZ")
        
        if(alu.zero_flag):
            bus.update(instructions_register.output[4:])
            draw_bus()
            pc.jump(bus)
            draw_program_counter()
            print("     IO J")
        else: print("     NC")
        tick()
    elif(x == 14):
        #OUT
        print("OUT")
        print("    ",array_to_decimal(a_register.output))
    elif(x == 15):
        #HLT
        print("HLT")
        exit()
 

def multiply(ram):
    ram.registers[0].update(parse_bits("1 0001 00001101"))#lda A
    ram.registers[1].update(parse_bits("1 0011 00001111"))#sub 1
    ram.registers[2].update(parse_bits("1 0111 00000110"))#jc 6
    ram.registers[3].update(parse_bits("1 0001 00001100"))#lda 0
    ram.registers[4].update(parse_bits("1 1110 00000000"))#out
    ram.registers[5].update(parse_bits("1 1111 00000000"))#hlt
    ram.registers[6].update(parse_bits("1 0100 00001101"))#sta A
    ram.registers[7].update(parse_bits("1 0001 00001110"))#lda B
    ram.registers[8].update(parse_bits("1 0010 00001100"))#add 0
    ram.registers[9].update(parse_bits("1 0100 00001100"))#sta 0
    ram.registers[10].update(parse_bits("1 0110 00000000"))#j 0

    ram.registers[12].update(parse_bits("1 0000 00000000"))#0
    ram.registers[13].update(parse_bits("1 0000 00001101"))#A 13
    ram.registers[14].update(parse_bits("1 0000 00001001"))#B 9
    ram.registers[15].update(parse_bits("1 0000 00000001"))#1
    """
        #include <stdio.h>
        #define ADD(a, b, carry) a = a + b; carry = !!(a & 0x100); a &= 0xff
        #define SUB(a, b, carry) a = a + ((0xff ^ b) + 1); carry = !!(a & 0x100); a &= 0xff

        int a;           // 8-bit register A
        int carry;       // carry bit

        int M12 =  0;    // 8-bit accumulator
        int M13 = 20;    // input 1
        int M14 =  3;    // input 2
        int M15 =  1;    // 8-bit constant 1

        while (1) {
            // LDA [13]
            a = M13;

            // SUB [15]
            SUB(a, M15, carry);

            // JC
            if (!carry) {
                // LDA [12]
                a = M12;
                // OUT
                printf("OUT: %d\n", a);

                // HLT
                break;
            }

            // STA [13]
            M13 = a;

            // LDA [14]
            a = M14;

            // ADD [12]
            ADD(a, M12, carry);

            // STA [12]
            M12 = a;

            // JMP
        }
        
        return 0;
    """

myfont = pygame.font.SysFont("monospace", 15)
text_color = (0,0,0)

def draw_a_register(out = False):
        for i in range(len(a_register.output)):
            pygame.draw.line(win,(234*a_register.output[i],12,12), (800+i*12,60),(800+i*12,260) )
        pygame.draw.rect(win, (200,200,200),(780,60,130,60))
        label = myfont.render("A-Register", 1, text_color)
        win.blit(label, (795, 75))
        for i,j in enumerate(a_register.output):
            pygame.draw.circle(win, (234*j,12,12),(800+i*12,100),5)
            pygame.draw.line(win, (234*j,0,0),(910,70+i*6),(995-6*i,70+i*6))
    
def draw_b_register():
        for i in range(len(b_register.output)):
            pygame.draw.line(win,(234*b_register.output[i],12,12), (800+i*12,460),(800+i*12,330) )
        pygame.draw.rect(win, (200,200,200),(780,460,130,60))
        label = myfont.render("B-Register", 1, text_color)
        win.blit(label, (795, 475))
        for i,j in enumerate(b_register.output):
            pygame.draw.circle(win, (234*j,12,12),(800+i*12,500),5)

def draw_alu(out = False):
        pygame.draw.rect(win, (200,200,200),(765,260,130,70))
        
        label = myfont.render("ALU", 1, text_color)
        win.blit(label, (795, 275))
        pygame.draw.circle(win, (234*alu.carry_flag,12,12),(778,300),5)
        pygame.draw.rect(win, (200,200,200), (680,260,20,70))
        for i,j in enumerate(alu.output):
            pygame.draw.circle(win, (234*j,12,12),(800+i*12,300),5)
            pygame.draw.line(win,(234*j,12,12),(765,270+i*7),(700,270+i*7))
            pygame.draw.line(win,(out*234*j,12,12),(679,270+i*7),(680-56+i*7,270+i*7))
            pygame.draw.line(win,(out*234*j,12,12),(680-56+i*7,270+i*7),(680-56+i*7,400+i*7))
            pygame.draw.line(win,(out*234*j,12,12),(680-56+i*7,400+i*7),(400+(i+4)*12,400+i*7))
            pygame.draw.circle(win, (out*234*j,12,12),(400+(i+4)*12,400+i*7),2)


def draw_bus():
        pygame.draw.rect(win, (200,200,200),(390,40,150,70))
        pygame.draw.rect(win, 0,(390,80,53,30),1)
        pygame.draw.rect(win, 0,(390+52,80,99,30),1)
        offset = 0
        if(len(bus.output)==8):
            offset = 4
            for i in range(4):
                pygame.draw.line(win,0,(400+i*12, 110),(400+i*12, 930))
                pygame.draw.circle(win, 0, (400+i*12,100),5)
        
        for i in range(len(bus.output)):
            pygame.draw.circle(win, (253*bus.output[i],0,0), (400+(i+offset)*12,100),5)
            pygame.draw.line(win,(bus.output[i]*255,0,0),(400+(i+offset)*12, 110),(400+(i+offset)*12, 930))
        label = myfont.render("BUS", 1, text_color)
        win.blit(label, (400, 40))
        label = myfont.render("Instr.", 1, text_color)
        win.blit(label, (390, 80))
        label = myfont.render("Data", 1, text_color)
        win.blit(label, (460, 80))

        for i in range(8):
            pygame.draw.line(win, (bus.output[len(bus.output)-1-i]*253,0,0),(780,70+i*6),(700+i*6,70+i*6))
            pygame.draw.line(win, (bus.output[len(bus.output)-1-i]*253,0,0),(700+i*6,70+i*6),(700+i*6,140+i*6+60))
            pygame.draw.line(win, (bus.output[len(bus.output)-1-i]*253,0,0),(700+i*6,140+i*6+60),(400+(11-i)*12,140+i*6+60))
            pygame.draw.circle(win, (bus.output[len(bus.output)-1-i]*253,0,0), (400+(11-i)*12,140+i*6+60),2)
            #B Register
            pygame.draw.line(win, (bus.output[len(bus.output)-1-i]*253,0,0),(780,470+i*6),(400+(11-i)*12,470+i*6))
            pygame.draw.circle(win, (bus.output[len(bus.output)-1-i]*253,0,0), (400+(11-i)*12,470+i*6),2)
            #RAM
            pygame.draw.line(win, (bus.output[len(bus.output)-1-i]*253,0,0), (250,120+i*7),(580-(i+4)*12,120+i*7))
            pygame.draw.circle(win, (bus.output[len(bus.output)-1-i]*253,0,0),(580-(i+4)*12,120+i*7),2)
            

def draw_ram(out=False):
        pygame.draw.rect(win, (200,200,200),(100,110,150,70))
        pygame.draw.rect(win, (200,200,200),(100,250,150,70))
        label = myfont.render("Memory Address", 1, text_color)
        win.blit(label, (100, 110))
        label = myfont.render("Dec:"+str(array_to_decimal(ram.address_memory.output)), 1, text_color)
        win.blit(label, (100, 150))        
        for i in range(8):
            pygame.draw.circle(win, (ram.address_memory.output[i]*253,0,0), (107+i*12,140),5)
            pygame.draw.circle(win, (ram.registers[array_to_decimal(ram.address_memory.output)].output[i+4]*253,0,0), (107+i*12,290),5)
            pygame.draw.line(win, (ram.address_memory.output[i]*253,0,0),(107+i*12,180),(107+i*12,249))
            #pygame.draw.line(win, (ram.registers[array_to_decimal(ram.address_memory.output)].output[4+i]*253,0,0), (250,260+i*7),(400+(i+4)*12,260+i*7))
            pygame.draw.line(win,(ram.registers[array_to_decimal(ram.address_memory.output)].output[4+i]*253,0,0),(250,260+i*7),(300,260+i*7))
            pygame.draw.line(win,(out*ram.registers[array_to_decimal(ram.address_memory.output)].output[4+i]*253*out,0,0),(320,260+i*7),(400+(i+4)*12,260+i*7))
            pygame.draw.rect(win,(200,200,200),(300,250,20,70))
            pygame.draw.circle(win, (out*ram.registers[array_to_decimal(ram.address_memory.output)].output[4+i]*253,0,0),(400+(i+4)*12,260+i*7),2)
        label = myfont.render("Data", 1, text_color)
        win.blit(label, (100, 250))
        label = myfont.render("Dec:"+str(array_to_decimal(ram.registers[array_to_decimal(ram.address_memory.output)].output)), 1, text_color)
        win.blit(label, (100, 300))

def draw_program_counter(out=False):
    pygame.draw.rect(win, (200,200,200),(100,850,150,70))
    pygame.draw.rect(win,(200,200,200),(300,850,20,70))
    for i in range(8):
        pygame.draw.circle(win, (pc.counter.output[i]*253,0,0), (107+i*12,890),5)
        pygame.draw.line(win,(pc.counter.output[i]*253,0,0),(250,860+i*7),(300,860+i*7))
        pygame.draw.line(win,(out*pc.counter.output[i]*253*out,0,0),(320,860+i*7),(400+(i+4)*12,860+i*7))
        pygame.draw.circle(win, (out*pc.counter.output[i]*253,0,0),(400+(i+4)*12,860+i*7),2)
    label = myfont.render("Program Counter", 1, text_color)
    win.blit(label, (100, 850))
    label = myfont.render("Dec:"+str(array_to_decimal(pc.counter.output)), 1, text_color)
    win.blit(label, (100, 900))
#TODO ram input output check


TICK = False
def tick(x = 0.05):
    return
    pygame.display.flip()
    time.sleep(x)
    if(TICK):
        x = True
        while(x):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    x = False


if __name__ == "__main__":

    win = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Racing game")
    clock = pygame.time.Clock()

    #--------components---------#
    bus = Bus(8,[])

    pc = ProgramCounter()
    pc.counter.update([True]+bus.output)
    ram = RAM([])
    multiply(ram)
    ram.address_in(bus)  
    
    instructions_register = DynamicRegister(12,[])

    a_register = DynamicRegister(8, parse_bits("1 00000000"))
    b_register = DynamicRegister(8, parse_bits("1 00000000"))

    alu = Alu(8)
    alu.update(a_register.output+b_register.output+[False])
     
    while True:
        win.fill((125,124, 110))
        #fetch instructions from memory
        draw_a_register()
        draw_b_register()
        draw_alu()
        draw_bus()
        draw_ram()
        draw_program_counter()

        print("FETCH")
        pc.counter_out(bus)
        ram.address_in(bus)
        draw_program_counter(True)
        draw_bus()
        draw_ram()
        print("     CO MI")
        tick()

        draw_program_counter()
        ram.ram_out(bus)
        draw_ram(True)
        draw_bus()
        instructions_register.update([True]+bus.output)
        pc.count_enable()
        draw_program_counter()
        print("     RO II CE")
        #draw instrctions register
        tick()
        draw_ram()
        next_instruction(array_to_decimal(instructions_register.output[:4]))
        pygame.display.flip()

    

