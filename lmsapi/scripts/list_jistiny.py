import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api_customer.models import Customers
from api_cash.models import Cash


def dtstr_to_unix(string_date):
    return datetime.datetime.strptime(string_date, "%d/%m/%Y").timestamp()


def show_jistiny():
    start_date = dtstr_to_unix('01/01/2021')
    stop_date = dtstr_to_unix('31/12/2021')
    jistiny = Cash.objects.filter(comment__icontains='jistin', time__gte=start_date, time__lte=stop_date)
    total_value = 0
    for row in jistiny:
        total_value += row.value
        human_date = datetime.datetime.utcfromtimestamp(row.time).strftime('%Y-%m-%d %H:%M:%S')
        print(f'Datum: {human_date} User: {row.customerid} text: {row.comment} castka: {row.value} typ: {row.type}')
    print(f'Celkem: {total_value}')

def run():
    debtors = Customers.objects.filter(deleted=False)
    for debtor in debtors:

        crea_date = debtor.creationdate
        start_date = dtstr_to_unix('01/01/2022')
        if crea_date >= start_date:
            print(f'User: {debtor.id} ({debtor.lastname} {debtor.name}) jistina: {debtor.deposit}')


if __name__ == "__main__":
    # run()
    show_jistiny()
