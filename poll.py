while True:
    print(f"Enter one reason you like programming")
    reason = input()
    with open('poll.txt','a') as poll:
        poll.write(f"The reason is {reason}.\n")