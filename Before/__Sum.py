if __name__ == '__main__':
    # 1-50的累加和
    a = 0
    for i in range(1, 51):
        a += i
    print(a)
    # 1-50之间的偶数
    sum = 0
    for i in range(1, 51):
        if i % 2 == 0:
            sum += i
    print(sum)
