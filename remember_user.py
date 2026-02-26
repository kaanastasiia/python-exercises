import json

def get_name(name):
    with open('user_name.txt','a') as users:
        print(users)
        for u in users:
            if u != name:
                users.write(name + "\n")
        print(f"Nice to meet you, {name}!")

def greet_user(name):
    try:
        with open('user_name.txt') as user:
            for n in user:
                if n == name:
                    print(f"Hello, {name}!")
            get_name(name)
    except FileNotFoundError:
        get_name(name)

def main():
    name = input("Hello! What's your name? ")
    greet_user(name)

if __name__=="__main__":
    main()