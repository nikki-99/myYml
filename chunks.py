from json import load
import yaml

with open("demo6.yml","r")as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data['user'])

def chunks(lst, n):
    for i in range(0,len(lst),n):
        yield lst[i: i+n]

for account in chunks(data['user'], 3):
    print(account)