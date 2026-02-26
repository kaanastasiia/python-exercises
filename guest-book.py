while True:
    print(f"Please enter your name")
    name = input()
    print(f"Hello, {name}!")
    with open('guest-book.txt','a') as entry:
        entry.write(f"{name} has visited.\n")