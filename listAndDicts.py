def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Jose", "lastname": "Caicedo"}

    super_list = [
        {"firstname": "Jose", "lastname": "Caicedo"},
        {"firstname": "Luis", "lastname": "Ramirez"},
        {"firstname": "Andres", "lastname": "Rojas"},
        {"firstname": "Felipe", "lastname": "Fajardo"},
        {"firstname": "Stephanie", "lastname": "Rojas"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, ">", value)

    for item in super_list:
        print(item["firstname"], item["lastname"])


if __name__ == '__main__':
    run()
