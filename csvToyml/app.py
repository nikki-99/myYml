import csv
import yaml

# with open("tk.csv","w", newline='')as f:
#     writer = csv.writer(f)
#     writer.writerow(['Name','Age'])
#     writer.writerow(['Nikita',23])
#     writer.writerow(['Amit',22])
#     writer.writerow(['Anshu',22])

with open('tk.csv',"r")as f:
    datas = csv.reader(f)
    l=[]
    for data in datas:
        l=data
        break
    print(l)
    # next(datas)
    dct=[]
    for data in datas:
        d={}
        d[l[0]]=data[0]
        d[l[1]]=data[1]
        dct.append(d)

    print(dct)

with open('tk1.yaml',"w")as f:
    yaml.dump(dct,f)