if __name__ == '__main__':
    # 输入用户名和密码，超过三次账户被锁定
    for time in range(1, 4):
        name = input('用户名：')
        keyword = input('密码：')
        if name == 'admin' and keyword == '1234':
            print('登陆成功')
            break
        elif time < 3:
            print('用户名或密码错误')
        else:
            print('被锁定!')
