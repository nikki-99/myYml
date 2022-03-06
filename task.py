import csv

file ="main.csv"

def create():
    with open(file,"w",newline='')as f:
        writer = csv.writer(f)
        writer.writerow(['Name','Age','City'])
        writer.writerow(['Amit','23','Noida'])
        writer.writerow(['Nikita','23','Kolkata'])


def show():
    with open(file,"r")as f:
        row = csv.reader(f)
        for r in row:
            print(r)

def write():
    data=[]
    with open(file,"r") as f:
        row = csv.reader(f)
        for r in row:
            l=[]
            for i in r:
                l.append(i)
            data.append(l)
    print(data)
    with open(file,"w", newline='')as f:
        writer = csv.writer(f)
        for x in data:
            writer.writerow(x)
        writer.writerow(['Anshu','23','Ranchi'])
        

if __name__ == '__main__':
    # create()
    show()
    # write()
