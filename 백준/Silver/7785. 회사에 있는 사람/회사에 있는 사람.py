n = int(input())
logs = [input().split() for _ in range(n)]

work_dict = {}

for log in logs:
    if log[1] == 'enter':
        work_dict[log[0]] = True
    elif log[1] == 'leave':
        if log[0] in work_dict:
            del work_dict[log[0]]

for name in sorted(work_dict.keys(), reverse=True):
    print(name)
