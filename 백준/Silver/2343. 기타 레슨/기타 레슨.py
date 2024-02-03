import sys

def required_blu_rays(lectures, max_length):
    count = 1
    current_length = 0

    for lecture in lectures:
        if current_length + lecture > max_length:
            count += 1
            current_length = 0
        current_length += lecture

    return count

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lectures = list(map(int, input().rstrip().split()))

min_length, max_length = max(lectures), sum(lectures)

while min_length <= max_length:
    potential_length = (min_length + max_length) // 2
    if required_blu_rays(lectures, potential_length) > m:
        min_length = potential_length + 1
    else:
        max_length = potential_length - 1

print(min_length)