import sys

matrix = [sys.stdin.readline().rstrip().split() for _ in range(9)]
final_goal = matrix[4][4]  # (4,4)
mid_positions = [(3,3), (3,4), (3,5), (4,3), (4,5),(5,3), (5,4), (5,5)]
mid_goals = [matrix[r][c] for (r,c) in mid_positions]
def custom_key(s):
    def char_map(ch):
        if ch.isdigit():
            return (0, ord(ch))
        elif 'A' <= ch <= 'Z':
            return (1, ord(ch))
        else:
            return (2, ord(ch))
    mapped = [char_map(ch) for ch in s]
    return (mapped, len(s))
mid_details = {}
positions_of = {}
for r in range(9):
    for c in range(9):
        val = matrix[r][c]
        if val in mid_goals:  
            positions_of.setdefault(val, []).append((r,c))
for mg in mid_goals:
    coords = positions_of[mg]
    outside = None
    for (r,c) in coords:
        if not (3 <= r <= 5 and 3 <= c <= 5):
            outside = (r,c)
            break
    br = (outside[0] // 3)
    bc = (outside[1] // 3)
    row_start = 3*br
    col_start = 3*bc
    details = []
    for rr in range(row_start, row_start+3):
        for cc in range(col_start, col_start+3):
            if (rr, cc) != outside:
                details.append(matrix[rr][cc])
    mid_details[mg] = details
mid_goals.sort(key=custom_key)
for mg in mid_goals:
    mid_details[mg].sort(key=custom_key)
for i, mg in enumerate(mid_goals, start=1):
    print(f"#{i}. {mg}")
    details = mid_details[mg]
    for j, d in enumerate(details, start=1):
        print(f"#{i}-{j}. {d}")