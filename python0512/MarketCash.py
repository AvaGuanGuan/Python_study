if __name__ == '__main__':
    container = []
    sum_price = 0
    sum_count = 0
    flag = True
    while flag:
        name = input('商品名称：')
        price = input('商品价格：')
        number = input('商品数量:')
        sum_count += int(number)
        sum_price += int(price) * int(number)
        goods = [name, price, number]
        container.append(goods)
        answer = input('是否继续添加？（按q或Q退出）')
        if answer.lower() == 'q':
            flag = False
        print('*' * 30)
        print('名称\t价格\t数量')
    for goods in container:
        print('{}\t{}\t{}'.format(goods[0], float(goods[1]), int(goods[2])))
    print('一共买了%s件商品，共花费%s元' % (sum_count, sum_price))
