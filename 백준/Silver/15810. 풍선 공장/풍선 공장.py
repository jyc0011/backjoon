def balloons_in_time(staff_times, time):
    total_balloons = 0
    for t in staff_times:
        total_balloons += time // t
    return total_balloons

def min_time_to_make_balloons(N, M, staff_times):
    left, right = 0, max(staff_times) * M

    while left <= right:
        mid = (left + right) // 2
        total = balloons_in_time(staff_times, mid)

        if total >= M:
            right = mid - 1
        else:
            left = mid + 1

    return left

N, M = map(int, input().split())
staff_times = list(map(int, input().split()))

print(min_time_to_make_balloons(N, M, staff_times))
