def run():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    # # Used with list comprehensions
    # odd = [i for i in my_list if i % 2 != 0]

    # Used Filter
    odd = list(filter(lambda x: x % 2 != 0, my_list))

    # print
    print(odd)


if __name__ == '__main__':
    run()
