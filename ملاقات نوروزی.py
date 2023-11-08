x1, x2, x3 = map(float, input().split())

positions = sorted([x1, x2, x3])

total_distance = positions[2] - positions[0]

print(int(total_distance))
