def get_alphabet_distance(s1, s2):
    distance_list = []
    for char_s1, char_s2 in zip(s1, s2):
        distance = ord(char_s2) - ord(char_s1)
        if distance < 0:
            distance += 26
        distance_list.append(distance)
    return distance_list

t = int(input().strip())
for _ in range(t):
    s1, s2 = input().split()
    distances = get_alphabet_distance(s1, s2)
    print("Distances: " + " ".join(str(d) for d in distances))
