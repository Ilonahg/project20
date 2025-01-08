# generators/transactions.py
def filter_by_currency(transactions, currency):
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start, stop):
    for num in range(start, stop + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:]
