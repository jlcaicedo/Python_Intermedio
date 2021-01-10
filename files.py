def read():
    numbers = []
    with open("./archives/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Facundo", "Gregorio", "Marta", "Susana", "Jose"]
    with open("./archives/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    # this create a new file "names.txt
    write()


if __name__ == '__main__':
    run()
