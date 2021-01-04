def run():
    my_list = [1, 2, 3, 4, 5]

    # # List comprehensions
    # all_multiplied = 1
    # for i in my_list:
    #     all_multiplied = all_multiplied * i

    # used with reduce
    from functools import reduce
    all_multiplied = reduce(lambda a, b: a * b, my_list)

    # print
    print(all_multiplied)


if __name__ == '__main__':
    run()
