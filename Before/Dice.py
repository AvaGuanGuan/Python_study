if __name__ == '__main__':
    # 掷骰子:请输入充值金额,您现在有xx金币,请输入10的整数倍,请选择大小 ,两个骰子的点数,您猜对or错,当前金币xx,是否继续玩,剩余金币,游戏局数
    import random

    coin = 0
    time = 0
    while coin == 0:
        tmp = int(input('请输入您要充值的数量：'))
        if tmp % 10 == 0:
            print('充值成功!恭喜您拥有%d个金币' % (tmp))
            coin = tmp
        else:
            print('请输入正确的充值金额，只能充值10的倍数！')
    print('参与一次游戏将获得金币一枚！')
    while coin > 5:
        number = random.randint(2, 12)
        guess = int(input('大：0，小：1\n大还是小: '))
        time += 1
        coin -= 4
        if number >= 6 and guess == 0:
            coin += 2
            print('恭喜猜对了,获得金币两枚')
            print('您的剩余金币为：%d,共计玩了%d次' % (coin, time))
        elif number <= 6 and guess == 1:
            coin += 2
            print('恭喜猜对了,获得金币两枚')
            print('您的剩余金币为：%d,共计玩了%d次' % (coin, time))
        elif number >= 6 and guess == 1:
            print('很遗憾，没猜中')
            print('您的剩余金币为：%d,共计玩了%d次' % (coin, time))
        else:
            print('很遗憾，没猜中')
            print('您的剩余金币为：%d,共计玩了%d次' % (coin, time))
        play = input('继续：任意键，退出：N\n是否退出游戏：')
        if play == 'N':
            print('期待您下次再来')
            break
