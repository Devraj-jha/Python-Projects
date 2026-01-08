class Bank_account:
    def __init__(self,name, balance):
        self.name = name
        self.bal = balance


account1 = Bank_account("dj", 1000)
account2 = Bank_account("djjha", 10000)
print(account1)
accounts = []
for i in range(1000):
    accounts.append(Bank_account(f"user{i}", 0))

# print(accounts)
#self is the object itself. 

class Player:
    def set_data(self, health, x, y):
        self.health = health
        self.x = x
        self.y = y

p = Player()
p.set_data(100, 0, 0)
print(p.health)
