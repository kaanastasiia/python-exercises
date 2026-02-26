total = 0

with open('steam_navigation.txt') as book:
    for line in book:
       int_result = line.lower().count('the')
       total += int_result
       
print(f"The total count is {total}")