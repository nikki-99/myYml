import yaml

def yaml_loader(filepath):
    with open(filepath, "r") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
    return data

def yaml_dump(filepath, data):
    with open(filepath, "w")as f:
        yaml.dump(data,f)


if __name__== "__main__":
    filepath="demo3.yml"
    data = yaml_loader(filepath)
    print(data)

    items= data.get('items')
    for item_name, item_val in items.items():
        print(item_name,end=" ")
        print(item_val)


    # filepath1 = "demo4.yml"
    # data2={
    #     'items':{
    #         "sword":100,
    #         "axe":80,
    #         "boots":40
    #     }
    # }
    # yaml_dump(filepath1, data2)

    filepath2="demo5.yml"

    persons=[
        {"name": "Nikita", "age": 22},
        {"name": "Amit", "age": 22}
    ]

    yaml_dump(filepath2,persons)
