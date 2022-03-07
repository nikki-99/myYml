from importlib.abc import Loader
import yaml
import csv

names=[]
ages=[]

with open('tk1.yml',"r")as f:
    datas = yaml.load(f, Loader= yaml.FullLoader)
    for data in datas:
        names.append(data['name'])
        ages.append(data['age'])

with open("tk3.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(['Name','Age'])
    for i in range(len(names)):
        writer.writerow([names[i], ages[i]])