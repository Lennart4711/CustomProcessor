# CustomProcessor
## General info
This simulation is not using a clock. Clocks are used with physical hardware to ensure that all components execute their task before another task is given. Because computers work through their steps one by one, it is not possible for one step to be interrupted by another. Hardware latencies are therefore not simulated.
## Register info
A register is just a bunch of data latches. Because this simulation does not use a clock, as stated above, there is no edge triggered data flip flop. To **store data** set the **first bit** in the arguments to **true**
Also, there is **no dynamic ram** because the ram would not lose its charge. So static registers can and should be used as RAM.
## RAM info
I had to make a decision wether to loop over every register in ram when storing data and only storing it, where the address matches or to convert the binary address to a decimal number and access it directly through the list. I decided to convert it, because it keeps the programm scalable. I could do this in parallel to mimic the real world behaviour but I decided I don't want to do that.
## Instruction register 
The instruction register calls the functions of the components, no iteration over components and checking there
## Programm counter
I am going with a  rather unconventional aproach on the counter. I am not chaining a bunch of JK flip flops together, make shure there is no racing condition ... Instead of this the PC is going to consist of an Adder and a Register. So on Count Enable, I am going to store the register value plus one back in the register. On Counter out I am going to write the register value to the bus