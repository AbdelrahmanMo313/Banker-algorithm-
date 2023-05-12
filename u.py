import numpy as np
import ui2
import ui3
import ui4
import ui5
class Banker:

    def __init__(self):
        self.Total = ui4.Total
        self.maximum = ui2.Max
        self.allocation = ui3.Alloc
        self.available = np.empty((1, len(self.Total[0])), int)
        for i in range(len(self.Total[0])):
            self.available[0][i] = self.Total[0][i] - sum(self.allocation[:,i])
        self.need = [[self.maximum[i][j] - self.allocation[i][j] for j in range(len(self.maximum[0]))] for i in range(len(self.maximum))]

        self.allocation[ui5.pNum][ui5.rNum] += ui5.number


    def is_safe_state(self):
        finish = [False] * len(self.allocation)
        seq = []
        while False in finish:
            for i in range(len(self.allocation)):
                for j in range(len(self.allocation[0])):
                    if not finish[i] and self.need[i][j] <= self.available[0][j]:
                        finish[i] = True
                        seq.append(i+1)
                        self.AddValue(i)

        return seq

    def check(self, work):
        for i in range(len(self.allocation)):
            for j in range(len(work)):
                if self.need[i][j] > work[j].all():
                    return False
        return True

    def AddValue(self, proc):
        for i in range(len(self.available[0])):
            self.available[0][i] += self.allocation[proc][i]