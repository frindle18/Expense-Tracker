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
        self.account = 'Main'

    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type
        print(f'Default transaction type set to {self.transaction_type}, type u to undo')

    def set_account(self, account):
        self.account = account
        print(f'Default account set to {self.account}, type u to undo')

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

if __name__ == '__main__':
    main()
