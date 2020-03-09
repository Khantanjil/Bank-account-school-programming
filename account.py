class Account:

    def __init__(self, filepath, name):
        self.filepath = filepath
        self.name = name
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def showQuantity(self):
        return self.balance

    def __repr__(self, filepath, name):
        return f'The account user: {name}\nThe file text: {filepath}'
john_account = Account("john_acc.txt", "jack")
print(john_account.showQuantity())
