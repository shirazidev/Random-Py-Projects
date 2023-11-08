a = int(input())
b = [int(x) for x in input().split()]
count = 0
for i in range(a):
    if b[i] <= 2:
        count += 1
print(int(count/3))
