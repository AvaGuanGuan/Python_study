if __name__ == '__main__':
    # 随机生成一个整数，输入猜测的数字，记录回合数，如果猜大了就提示猜大了，猜中了就说恭喜
    import random

    numbers = random.randint(1, 100)
    time = 0
    guess = int(input('请输入猜测的数字：'))
    # time += 1
    while numbers != guess:
        # guess = int(input('请输入猜测的数字：'))
        time += 1
        if guess > numbers:
            print('猜大了！')
            guess = int(input('请输入猜测的数字：'))
            continue
        if guess < numbers:
            print('猜小了！')
            guess = int(input('请输入猜测的数字：'))
    time += 1
    print('恭喜您！%d次就猜对了！' % time)
