if __name__ == '__main__':
    # 随机生成二维码
    import random

    filename = ''
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(6):
        index = random.randint(0, len(a) - 1)
        filename += a[index]
    print(filename)
