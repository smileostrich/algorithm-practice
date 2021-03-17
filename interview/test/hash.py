hash = {}


def find(key):
    return hash.get(key)


def add(key, value):
    hash.update({key: value})


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        for i in range(N):
            key, value = map(str, input().split())
            add(key, value)

        print("#%d" % test_case)

        Q = int(input())

        for i in range(Q):
            key = input()
            key = key.strip(" ")
            value = find(key)
            if value:
                print(value)
            else:
                print("not find")


if __name__ == "__main__":
    main()