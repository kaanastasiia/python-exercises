from random import choice

lottery = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]

winning_combination = [] 

my_ticket = []

for i in range(4):
    my_ticket.append(choice(lottery))

guesses = 0

while True:
    guesses += 1
    winning_combination = []
    for i in range(4):
        winning_combination.append(choice(lottery))
    if my_ticket == winning_combination:
        break


print(f"Your ticket took {guesses} guesses to win")
