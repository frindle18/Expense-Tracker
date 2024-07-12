from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount, account, reason, note):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now().strftime('%d-%m-%Y')
        self.account = account
        self.reason = reason
        self.note = note

    def __repr__(self):
        return (f'Transaction(type={self.transaction_type}, amount={self.amount}, date={self.date}, account={self.account}, reason={self.reason}, note={self.note})')
    
class ExpenseTracker:
    def __init__(self):
        self.transaction_type = '-'
        self.account = 'Main'

    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type
        print(f'Default transaction type set to {self.transaction_type}, type u to undo')

    def set_account(self, account):
        self.account = account
        print(f'Default account set to {self.account}, type u to undo')
