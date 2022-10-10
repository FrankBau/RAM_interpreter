from atexit import register

class RAM:

    def __init__(self, source_code, input=[]):
        self.program = source_code.split('\n')
        self.pc = 0
        self.register = [0] * 1000 # a guess
        self.input = input
        self.output = []
        self.halted = False

    def step(self):
        if self.halted:
            return 0
        instruction = self.program[self.pc].split()
        opcode = instruction[0]
        if len(instruction) > 1:
            oparg = int(instruction[1])
        self.pc = self.pc + 1
        if opcode == 'READ':
            self.register[0] = self.input.pop(0)
        elif opcode == 'WRITE':
            print(self.register[0], end=' ')
            self.output.append(self.register[0])
        elif opcode == 'LOADIMM':
            self.register[0] = oparg
        elif opcode == 'LOAD':
            self.register[0] = self.register[oparg]
        elif opcode == 'STORE':
            self.register[oparg] = self.register[0]
        elif opcode == 'ADD':
            self.register[0] = self.register[0] + self.register[oparg]
        elif opcode == 'SUB':
            self.register[0] = self.register[0] - self.register[oparg]
        elif opcode == 'JUMP':
            self.pc = oparg
        elif opcode == 'JZERO':
            if self.register[0]==0:
                self.pc = oparg
        elif opcode == 'JGTZ':
            if self.register[0]>0:
                self.pc = oparg
        elif opcode == 'HALT':
            self.halted = True
            self.pc = self.pc - 1
            return False
        else:
            self.pc = self.pc - 1
            raise RuntimeError(f'illegal {instruction=}')
        return True

if __name__ == "__main__":

    import sys

    if len(sys.argv) < 2:
        print("usage: ram program.ram input1 input2 ...")
        sys.exit(1)

    file_name = sys.argv[1]
    file = open(file_name, mode='r')
    source_code = file.read()
    file.close()

    input = [int(i) for i in sys.argv[2:]]

    ram = RAM(source_code, input)

    while not ram.halted:
        ram.step()

    sys.exit(0)