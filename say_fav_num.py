import json

with open('fav-num.txt','r') as num:
    fav_num = json.load(num)
    print(fav_num)