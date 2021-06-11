class InsufficientAmount(Exception):
    pass

class NegativeAmount(Exception):
    pass
 

class Wallet(object):

    def __init__(self, initial_amount=0, currency='GBP'):
        self.value = initial_amount
        self.currency = currency


    def spend(self, amount):
        if self.value < amount:
            raise InsufficientAmount('Not enough funds available to spend, wallet contains: {}'.format(self.value))
        self.value -= amount


    def add(self, amount):
        if amount < 0:
            raise NegativeAmount('Can not deposit a negative amount: {}'.format(amount))
        self.value += amount


    def show_wallet(self):
        return {'Wallet value' : self.value, 'Currency' : self.currency}
