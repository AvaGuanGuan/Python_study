if __name__ == '__main__':
    # 模拟文件上传，输入上传文件的名称，判断文件名是否大于六位数，扩展名是否是：jpg,gif,png格式
    # 如果不是就提示上传失败，如果名字不满足条件而扩展名满足，则随机生成一个六位数的文件名，打印成功上传xxxxxx.png
    import random

    name = input('请输入文件名：')
    a = name.rfind('.')
    filename = name[a:]
    length = len(name)
    if length == 10:
        print('成功上传%s' % name)
    elif length != 10 and name.endswith == '.jpg' or '.gif' or ',png':
        rname = random.randint(100000, 999999)
        print('成功上传%d%s' % (rname, filename))
    else:
        print('上传失败！')
