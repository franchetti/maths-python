import time


def main(a, b):
    c = a + b
    print(c)
    time.sleep(1)
    main(b, c)


main(1, 1)
