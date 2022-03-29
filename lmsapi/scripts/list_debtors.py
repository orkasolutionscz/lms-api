from api_customer.models import Customers


def run():
    debtors = Customers.objects.filter(deleted=0)
    for debtor in debtors:
        balance = debtor.balance()
        if balance is None:
            balance = 0

        if balance < 0:
            name = debtor.full_name()
            print(f'User: {name} balance: {balance}')
