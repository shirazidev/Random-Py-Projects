n = int(input())

laptops = []
for _ in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))



for i in range(n):
    for j in range(n):
        if laptops[i][0] < laptops[j][0] and laptops[i][1] > laptops[j][1]:
            print("happy irsa")
            exit()



print("poor irsa")
