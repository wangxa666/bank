from bank.operation import Operation


def main():
    op = Operation()
    while True:
        print('*********欢迎进入中国银行****************')
        print('***********银行操作如下******************')
        print('**** 1.开户        2.查询****************')
        print('**** 3.存款        4.取款****************')
        print('**** 5.转账        6.改密****************')
        print('**** 7.锁卡        8.解卡****************')
        print('*** 9.销户        0.退出****************')
        print('*** A.保存数据')
        num = input('请输入您要执行的操作:')
        if num == '1':
            op.create_account()
        elif num == '2':
            op.query_account()
        elif num == '3':
            op.add_money()
        elif num == '4':
            op.sub_money()
        elif num == '5':
            op.transfer()
        elif num == '6':
            op.change_password()
        elif num == '7':
            op.lock_card()
        elif num == '8':
            op.unlock_card()
        elif num == '9':
            op.del_accout()
        elif num == '0':
            if op.tuichu():
                break
        elif num == 'A':
            op.save_data()
        else:
            print('您输入的不合法，请重新输入')


if __name__ == '__main__':
    main()
