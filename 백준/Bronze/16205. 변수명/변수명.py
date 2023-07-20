def convert(n, a):
    result = ["", "", ""]
    if n == "1":  # camelCase
        result[0] = a
        result[1] = "".join(["_" + i.lower() if i.isupper() else i for i in a])
        result[2] = a[0].upper() + a[1:]
    elif n == "2":  # snake_case
        words = a.split('_')
        result[0] = words[0] + "".join([i.capitalize() for i in words[1:]])
        result[1] = a
        result[2] = "".join([i.capitalize() for i in words])
    else:  # PascalCase
        result[0] = a[0].lower() + a[1:]
        result[1] = a[0].lower() + "".join(["_" + i.lower() if i.isupper() else i for i in a[1:]])
        result[2] = a
    return result

n, a = input().split()
output = convert(n, a)
for i in output:
    print(i)
