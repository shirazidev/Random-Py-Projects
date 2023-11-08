from math import sqrt
listA = []
n = int(input())
i = 0
while i < n:
 num = int(input())
 i += 1
 square = sqrt(num)
 square = "{:0.8f}".format(square)
 square = square[:-4]
 listA.append(square)


for square in listA:
    print(square) 
