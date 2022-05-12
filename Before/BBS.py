# 模拟论坛：昨天晚会遇到一个小姐姐，要不要表白？
# 输入用户名：小白
# 反复回复：1.回复内容不能为空。2.里面不能存在敏感词汇。3.最多评论20个字。4.回复的内容前后不能有空格
if __name__ == '__main__':
    message=input('发表内容：')
    print('-'*50)
    print('以下为回复内容：')
    while True:
        name=input('用户名：')
        while True:
            comment=input('评论：')
            comment=comment.strip()
            if len(comment)!=0:
                if len(comment)<=20:
                    comment=comment.replace('傻逼','**')
                    print('\t{}发表的评论是：{}'.format(name,comment))
                    break
                else:
                    print('请输入不超过20个字！')
            else:
                print('评论内容不能为空！')