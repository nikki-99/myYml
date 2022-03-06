import csv

# DictReader : gives a dictionary 

file = "name.csv"

html_output =''

with open(file, "r")as f:
    l=[]
    # row = csv.DictReader(f)
    row = csv.reader(f)
    # for r in row:
    #     print(r['Name'])

    # Don't want 'Name'
    next(row)

    for r in row:
        l.append(r[1])


html_output += f'<p>There are currently {len(l)} students.</p>'

html_output+= '\n<ul>'

for name in l:
    html_output+=f'\n\t<li>{name}</li>'

html_output+= '\n</ul>'

print(html_output)