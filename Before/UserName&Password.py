if __name__ == '__main__':
    flag = True
    while flag:
        name = input('用户名/手机号：')
        if (name.islower() and name[0].isalpha() and len(name) >= 6) or name.isdigit() and len(name) == 11:
            while True:
                password = input('密码：')
                if password.isdigit() and len(password) == 6:
                    if (name == 'admin123' or name == '15811119999') and password == 200325:
                        print('用户登录成功！')
                        flag = False
                        break
                    else:
                        print('用户名或者密码有误！')
                        break
                else:
                    print('密码必须是6位数字！')
        else:
            print('用户名或手机号格式错误！')
