heights = [int(input()) for _ in range(9)]
total = sum(heights)

for i in range(9):
    for j in range(i+1, 9):
        if total - (heights[i] + heights[j]) == 100:
            fake1, fake2 = heights[i], heights[j]

heights.remove(fake1)
heights.remove(fake2)
heights.sort()

for height in heights:
    print(height)