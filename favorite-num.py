import json

def store_fav_num():
    fav_num = input("What's your favourite number?")
    with open('fav-num.txt','w') as num:
        print(f"Noted! Your favourite number if {fav_num}")
        json.dump(fav_num,num)
        return fav_num

def return_fav_num():
    try:
        with open('fav-num.txt','r') as num:
            return json.load(num)
    except FileNotFoundError:
        return store_fav_num()

def main():
    fav_num = return_fav_num()
    print(f"Your favourite number is {fav_num}")

if __name__=="__main__":
    main()