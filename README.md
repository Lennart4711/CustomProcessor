# CustomProcessor
## General info
This simulation is not using a clock. Clocks are used with physical hardware to ensure that all components execute their task before another task is given. Because computers work through their steps one by one, it is not possible for one step to be interrupted by another. Hardware latencies are therefore not simulated.
## Register info
A register is just a bunch of data latches. Because this simulation does not use a clock, as stated above, there is no edge triggered data flip flop. To **store data** set the **first bit** in the arguments to **true**
Also, there is also **no dynamic ram** because the ram would not lose its charge. So static registers can and should be used as RAM