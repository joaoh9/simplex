import sys

from simplex import Tableaux

input_fie = open(sys.argv[1], "r")

T = Tableaux(input_fie.readline())

lines = input_fie.readlines()

i = 0
for line in lines:
    if i == 0:
        T.getC(line)
    else:
        T.getA_andB(line)
    i += 1

T.print_tableaux()
