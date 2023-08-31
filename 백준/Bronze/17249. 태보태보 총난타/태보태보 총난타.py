s = input()

face_idx = s.index('(^0^)')

left = s[:face_idx]
right = s[face_idx+5:]

left_count = left.count('@=')
right_count = right.count('=@')

print(left_count, right_count)