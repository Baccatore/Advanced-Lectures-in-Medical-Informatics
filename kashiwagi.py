import numpy as np
x, y, z = map(int,input().split())

answer = [[] for i in range(z)]
empty = [False for i in range(y+1)]

ex_line = empty
k=0
for i in range((x+1)*z):
    if i % (x+1) == x: 
        input()
        answer[k]=line
        ex_line = empty;
        k += 1
        continue
    else :
        line = input()
        line = [j == '#' for j in list(line)]
        line = np.logical_or(list(line), ex_line)
        ex_line = line

for i in range(z):
    answer[i] = ''.join(['#' if true else '.' for true in answer[i]])

answer.reverse()

for line in answer:
    print(line[:-1])
