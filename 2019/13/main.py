from collections import defaultdict

class IntcodeComputer(object):

    def __init__(self, pid, program_file, inputs):
        self.instructions = [int(x) for x in open(program_file).read().split(",")]
        self.inserts = inputs
        self.ip = 0
        self.pid = pid
        self.relative_base = 0
        self.outs = []

    def index(self, i, I):
        mode = (0 if i >= len(I) else I[i])
        val = self.instructions[self.ip+1+i]
        if mode == 0:
            pass
        elif mode == 1:
            assert False
        elif mode == 2:
            val += self.relative_base
        while len(self.instructions) <= val:
            self.instructions.append(0)
        return val
    def val(self, i, I):
        mode = (0 if i>=len(I) else I[i])
        val = self.instructions[self.ip+1+i]
        if mode == 0:
            val = self.instructions[val]
        elif mode == 2:
            val = self.instructions[val + self.relative_base]
        return val

    def run(self):
        while True:
            cmd = str(self.instructions[self.ip])
            opcode = int(cmd[-2:])
            I = list(reversed([int(x) for x in cmd[:-2]]))
            if opcode == 1:
                self.instructions[self.index(2, I)] = self.val(0, I) + self.val(1, I)
                self.ip += 4
            elif opcode == 2:
                self.instructions[self.index(2, I)] = self.val(0, I) * self.val(1, I)
                self.ip += 4
            elif opcode == 3:
                self.instructions[self.index(0, I)] = self.inserts[0]
                self.inserts.pop()
                self.ip += 2
            elif opcode == 4:
                ans = self.val(0, I)
                # self.outs.append(ans)
                # self.ip += 2
                return ans
            elif opcode == 5:
                self.ip = self.val(1, I) if self.val(0, I) != 0 else self.ip+3
            elif opcode == 6:
                self.ip = self.val(1, I) if self.val(0, I) == 0 else self.ip+3
            elif opcode == 7:
                self.instructions[self.index(2, I)] = (1 if self.val(0, I) < self.val(1, I) else 0)
                self.ip += 4
            elif opcode == 8:
                self.instructions[self.index(2, I)] = (1 if self.val(0, I) == self.val(1, I) else 0)
                self.ip += 4
            elif opcode == 9:
                self.relative_base += self.val(0, I)
                self.ip += 2
            else:
                assert opcode == 99, opcode
                # return self.outs
                return None


# program_runner = IntcodeComputer("0", "input", [1])
# outputs = program_runner.run()
# i = 1
# c = 0

# while i <= len(outputs):
#     if i % 3 == 0:
#         if outputs[i-1] == 2:
#             c += 1
#     i+=1

# print(outputs)
# print(c)  # part 1

G = defaultdict(int)
def make_inputs():
    # R = sorted([r for r,c in G])
    # C = sorted([c for r,c in G])
    for pos, v in G.items():
        if v == 3:
            paddle = pos
        if v == 4:
            ball = pos
    if ball[1] < paddle[1]:
        return -1
    elif ball[1] > paddle[1]:
        return 1
    else:
        return 0


P = IntcodeComputer("0", "input", make_inputs)

while True:
    x = P.run()
    y = P.run()
    c = P.run()
    if x == -1 and y == 0:
        print('Score', c)
    if x is None or y is None or c is None:
        break
    G[(y, x)] = c


ans = 0
for k, v in G.items():
    if v == 2:
        ans += 1

print(ans)


