print(f"What's your name?")
name = input()

with open('guests.txt','w') as guest:
    guest.write(f"Hello, {name}!")
