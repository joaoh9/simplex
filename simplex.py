class Identity:
    def __init__(self, N):
        self.id = []

        for i in range(N):
            self.id.append([])
            for j in range(N):
                if i == j:
                    self.id[i].append(1)
                else:
                    self.id[i].append(0)


class VERO:
    def __init__(self, size):
        self.upper = [0] * size
        self.identity = Identity(size)


class Tableaux:
    def __init__(self, line):
        NM = self.string_to_int_list(line)
        self.N = NM[0]
        self.M = NM[1]
        self.A = []
        self.B = []
        self.VERO = VERO(self.N)

    def getC(self, vector):
        self.C = self.string_to_int_list(vector)

    def getA_andB(self, line):
        row = self.string_to_int_list(line)
        self.A.append(row[:-1])
        self.B.append(row[-1])

    def string_to_int_list(self, string):
        return list(map(int, string.split(" ")))

    def print_tableaux(self):
        print(self.VERO.upper, self.C, 0)
        for i in range(self.N):
            print(self.VERO.identity.id[i], self.A[i], self.B[i])
