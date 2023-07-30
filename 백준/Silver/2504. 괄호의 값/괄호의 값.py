bracket_sequence = input()
sequence_length = len(bracket_sequence)
bracket_stack = []
multiplier = 1
result = 0

for i in range(sequence_length):
    current_bracket = bracket_sequence[i]
    
    if current_bracket == '(':
        multiplier *= 2
        bracket_stack.append(current_bracket)
    elif current_bracket == '[':
        multiplier *= 3
        bracket_stack.append(current_bracket)

    elif current_bracket == ')':
        if not bracket_stack or bracket_stack[-1] == '[':
            result = 0
            break
        if bracket_sequence[i-1] == '(':
            result += multiplier
        multiplier //= 2
        bracket_stack.pop()
        
    else:
        if not bracket_stack or bracket_stack[-1] == '(':
            result = 0
            break
        if bracket_sequence[i-1] == '[':
            result += multiplier
        multiplier //= 3
        bracket_stack.pop()

if bracket_stack:
    result = 0

print(result)
