from datetime import datetime
import re

class Transaction:
    def __init__(self, transaction_type, amount, date, reason, account, note):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date
        self.reason = reason
        self.account = account
        self.note = note

    def __repr__(self):
        return f'Transaction(transaction_type="{self.transaction_type}", amount={self.amount}, date="{self.date}", reason="{self.reason}", account="{self.account}", note="{self.note}")'

    def __str__(self):
        return f'{self.transaction_type}{self.amount} {self.date} {self.reason} {self.account} "{self.note}"'
    
class ExpenseTracker:
    def __init__(self):
        self.transaction_type = '-'
        self.transaction_type_history = [] # Undo
        self.transaction_type_log = [] # Redo
        self.account = 'Main'
        self.account_history = []
        self.account_log = []

    def set_transaction_type(self, transaction_type):
        self.transaction_type_history.append(self.transaction_type)
        self.transaction_type_log.clear()
        self.transaction_type = transaction_type
        print(f'Default transaction type set to {self.transaction_type}, type u to undo')

    def undo_set_transaction_type(self):
        if self.transaction_type_history:
            self.transaction_type_log.append(self.transaction_type)
            self.transaction_type = self.transaction_type_history.pop()
            print(f'Default transaction type reverted to {self.transaction_type}')

        else:
            print('No previous transaction type to undo')

    def redo_set_transaction_type(self):
        if self.transaction_type_log:
            self.transaction_type_history.append(self.transaction_type)
            self.transaction_type = self.transaction_type_log.pop()
            print(f'Default transaction_type set to {self.transaction_type}')
        else:
            print('No transaction_type to redo')

    def set_account(self, account):
        self.account_history.append(self.account)
        self.account_log.clear()
        self.account = account
        print(f'Default account set to {self.account}, type u to undo')

    def undo_set_account(self):
        if self.account_history:
            self.account_log.append(self.account)
            self.account = self.account_history.pop()
            print(f'Default account type reverted to {self.account}')
            
        else:
            print('No previous account type to undo')

    def redo_set_account(self):
        if self.account_log:
            self.account_history.append(self.account)
            self.account = self.account_log.pop()
            print(f'Default account set to {self.account}')
        else:
            print('No account to redo')

    def parse_transaction(self, command):
        pattern = re.compile(r'([+-])?(\d+)\s(\d+[.\/-]\d+[.\/-]\d+\s)?(\w+)\s(\w+\s)?(".*")?')
        match = pattern.match(command)

        transaction_type = match.group(1) if match.group(1) else self.transaction_type
        amount = match.group(2)
        date = match.group(3).strip() if match.group(3) else datetime.now().strftime('%d-%m-%Y')
        reason = match.group(4)
        account = match.group(5).strip() if match.group(5) else self.account
        note = match.group(6)[1:-1] if match.group(6) else None

        new_transaction = Transaction(transaction_type, amount, date, reason, account, note)
        print(new_transaction)

def main():
    et = ExpenseTracker()
    et.set_transaction_type('-')
    et.set_account('HDFC')

    et.parse_transaction('-100 13-07-2024 Tea IDBI "Stop drinking tea"')
    et.parse_transaction('100 Tea "Stop drinking tea"')

    et.set_account('IDBI')
    et.undo_set_account()
    et.undo_set_account()
    et.redo_set_account()
    et.redo_set_account()

if __name__ == '__main__':
    main()
