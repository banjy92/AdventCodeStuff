from .day import Day
import itertools


class Day17(Day):
    def __init__(self, inputList):
        super().__init__(inputList)

    def getAnswer(self, questionNum):
        return self.answerOne() if questionNum == 1 else self.answerTwo()

    def answerOne(self):
        return len(
            self.runCycle(
                6, 3,
                set((i, j, 0) for i, v in enumerate(self.inputList)
                    for j, w in enumerate(v) if w == "#")))

    def answerTwo(self):
        return len(
            self.runCycle(
                6, 4,
                set((i, j, 0, 0) for i, v in enumerate(self.inputList)
                    for j, w in enumerate(v) if w == "#")))

    def runCycle(self, cyc, dim, on):
        for _ in range(cyc):
            newon = set(
                p for p in itertools.product(*self.dimList(dim, on))
                if self.turnOn(p, self.countA(p, on, dim), on))

            on = newon

        return on

    def dimList(self, d, on):
        return [self.n_range(x, on) for x in range(d)]

    def turnOn(self, p, c, on):
        return c == 3 or (c == 2 and p in on)

    def n_range(self, i, l):
        return range(min(a[i] for a in l) - 1, max(a[i] for a in l) + 2)

    def countA(self, p, l, d):
        diff = [-1, 0, 1]
        c = sum([
            1 for pc in itertools.product(diff, repeat=d)
            if pc != (0, ) * d and tuple(x + y for x, y in zip(pc, p)) in l
        ])
        return c


if __name__ == '__main__':
    print("True")
