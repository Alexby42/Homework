import threading
lock = threading.Lock()
class BankAccount:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deposit = 1000
        #self.withdraw = withdraw
        #self.amount = 0
        #self.account = account
        #self.amount = amount
    def deposit_task(self, account, amount):
        with lock:
            for _ in range(5):
                self.deposit += amount
                #account.deposit(amount)
                print(f'Deposited {amount}, new balance is {account.deposit}')
    def withdraw_task(self, account, amount):
        with lock:
            for _ in range(5):
                self.deposit -= amount
                #account.withdraw(amount)
                #account = BankAccount()
                print(f'Withdraw {amount}, new balance is {account.deposit}')
account = BankAccount()
deposit_thread = threading.Thread(target=account.deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=account.withdraw_task, args=(account, 150))
deposit_thread.start()
withdraw_thread.start()
deposit_thread.join()
withdraw_thread.join()