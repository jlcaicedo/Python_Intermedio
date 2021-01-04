def run():
    ## Square Numbers
    # squares = []

    # for i in range(1, 101):

    ## Square Numbers dont divisible in 3
    #     if i % 3 != 0:
    #         squares.append(i ** 2)

    # List Conprehensions
    squares = [i ** 2 for i in range(1, 101) if i % 3 != 0]

    # List first 100 natural numbers with square raiz
    import math
    squarestask = {i: math.sqrt(i) for i in range(1, 1001)}

    print(squares)
    print(squarestask)


if __name__ == '__main__':
    run()
