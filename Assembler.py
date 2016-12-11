class writer:
    def __init__(self, path):
        with open(path,'w') as file:
            self.file = file


'''
blocks!
0-15 virtual registers
16-255 static variables
2048-16483 heap
16384-24575 memory mapped I/O

registers
ram[0] SP stack pointer
ram[1] LCL points to the current VM function
ram[2] ARG points the current function`s argument var
ram[3] THIS points to current this (in the heap)
ram[4] THAT points to current that (heap 2)
ram[5-12] hold conents of temp
ram[13-15] general purposes registers.

local, argument, this, that :

'''



class AssemblerFile:
    def __init__(self, content, path):
        self.content = content
        self.writer = writer(path)


