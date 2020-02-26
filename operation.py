import os
import pickle
import uuid

from bank.user import User


class Operation(object):
    def __init__(self):
        if os.path.exists('user_list.txt'):
            file = open('user_list.txt', 'rb')
            self.user_list = pickle.load(file)
            file.close()
        else:
            self.user_list = []

    def create_account(self):
        username = input('请输入用户名:')
        password = input('请输入密码:')
        card_id = self.gen_card_id()

        user = User(username, password, card_id)
        self.user_list.append(user)

        for u in self.user_list:
            print(u)

    @staticmethod
    def gen_card_id():
        card_id = str(uuid.uuid4())
        return card_id

    def is_exists(self, msg):
        card_id = input(msg)
        for user in self.user_list:
            if user.card_id == card_id:
                return user
        else:
            return None

    def query_account(self):
        user = self.is_exists('请输入您的卡号:')
        if user:
            password = input('请输入密码:')
            if user.check_password(password):
                msg = user.name + '卡上余额{}元'.format(user.money)
                if user.lock:
                    msg = '您的银行卡已被冻结！！！！' + msg
                    print(msg)

            else:
                print('密码错误！！！')
        else:
            print('您输入的卡号不存在')

    def add_money(self):
        user = self.is_exists('请输入您的卡号:')
        if user.lock:
            print('您的卡已经被冻结了，不能存入！！！！')
            return
        if user:
            money = input('请输入您要存入的金额:')
            user.money += float(money)
            print(user)
        else:
            print('您输入的卡号不存在')

    def sub_money(self):
        user = self.is_exists('请输入您的卡号:')
        if user:
            password = input('请输入密码:')
            if user.lock:
                print('您的卡号已经被冻结了，不能取钱！！！！')
                return
            if user.check_password(password):
                money = float(input('请输入您要取出的金额:'))
                if money > user.money:
                    print('余额不足!!!')
                else:
                    user.money -= money
                    print(user)
            else:
                print('密码错误！！！')
        else:
            print('您输入的卡号不存在')

    def transfer(self):
        user = self.is_exists('请输入要转出的银行卡号:')
        if user:
            password = input('请输入要转出的银行卡密码:')
            if user.check_password(password):
                rmb = float(input('请输入要转出的金额:'))
            else:
                print('要转出的银行卡密码错误！')
                return
        else:
            print('您要转出的银行卡不存在')
            return

        user2 = self.is_exists('请输入您要转入的卡号:')
        if user2:
            user.money -= rmb
            user2.money += rmb
        else:
            print('您要转入的卡号不存在！！！')

    def change_password(self):
        user = self.is_exists('请输入您要修改密码的卡号:')
        if user:
            old_password = input('请输入原来的密码:')
            if user.check_password(old_password):
                new_password = input('请输入新的密码:')
                user.password = new_password
                # user.set_password(new_password)
            else:
                print('密码输入错误！！！')

        else:
            print('您要修改密码的卡号不存在')

    def lock_card(self):
        user = self.is_exists('请输入您要冻结的卡号:')
        if user:
            user.lock = True
        else:
            print('您要冻结的卡号不存在!!!')

    def unlock_card(self):
        user = self.is_exists('请输入您要解锁的卡号:')
        if user:
            user.lock = False
        else:
            print('您要解锁的卡号不存在!!!')

    def del_accout(self):
        user = self.is_exists('请输入您要销户的卡号:')
        if user:
            self.user_list.remove(user)
        else:
            print('输入的卡号不存在')

    def tuichu(self):
        is_sure = input('您确定要退出吗?Y / N:  ')
        # if is_sure.lower() == 'y':
        #     return True
        # return False
        if is_sure.lower() == 'y':
            self.save_data()
            return True
        return False

    def save_data(self):
        file = open('user_list.txt', 'wb')
        # file.write(self.user_list)
        pickle.dump(self.user_list, file)
        file.close()
