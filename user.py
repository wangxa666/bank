import hashlib


class User(object):
    def __init__(self, name, password, card_id, money=0, lock=False):
        self.name = name
        self.card_id = card_id
        self.money = money
        self.lock = lock
        self.__password = self.__encrypt_password(password)

    def __str__(self):
        return '用户名{},余额{},卡号{}'.format(self.name, self.money, self.card_id)

    def check_password(self, password):
        return self.__password == self.__encrypt_password(password)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = self.__encrypt_password(new_password)

    # def set_password(self, new_password):
    #     self.__password = self.__encrypt_password(new_password)

    @staticmethod
    def __encrypt_password(password):
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        return m.hexdigest()
