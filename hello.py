import yaml



with open("demo4.yml","r") as f:
    data = yaml.load_all(f, Loader=yaml.FullLoader)
    print(next(data))
    print(next(data))