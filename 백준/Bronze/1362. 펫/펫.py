def execute_action(action, weight):
    action_type, number = action
    if action_type == 'E':
        weight -= int(number)
    elif action_type == 'F':
        weight += int(number)
    return weight

def check_pet_status(optimal_weight, weight):
    if weight <= 0:
        return "RIP"
    elif optimal_weight / 2 < weight < optimal_weight * 2:
        return ":-)"
    else:
        return ":-("

def simulate_pet():
    cnt = 0
    while True:
        optimal_weight, weight = map(int, input().split())
        if optimal_weight == 0 and weight == 0:
            break

        die = False
        while True:
            action = input().split()
            if action[0] == '#' and action[1] == '0':
                break

            if not die:
                weight = execute_action(action, weight)

            if weight <= 0:
                die = True

        cnt += 1
        print(f"{cnt} {check_pet_status(optimal_weight, weight)}")

simulate_pet()
