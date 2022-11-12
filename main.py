from decorators import *


@logger
@cacher
def seq(n):
    rez = list(map(lambda i: (i+1)**i, range(0, n+1)))
    return rez


def main():
    seq(3)
    seq(5)
    seq(7)
    seq(9)
    seq(11)
    seq(13)


if __name__ == '__main__':
    main()
