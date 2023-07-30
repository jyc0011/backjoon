V = int(input())
votes = input()

A_votes = votes.count('A')
B_votes = votes.count('B')

if A_votes > B_votes:
    print('A')
elif A_votes < B_votes:
    print('B')
else:
    print('Tie')
