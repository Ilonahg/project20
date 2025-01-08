def filter_by_currency(transactions, currency):
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start, stop):
    for num in range(start, stop + 1):
        formatted_number = f"{num:016d}"
        yield (
            f"{formatted_number[:4]} {formatted_number[4:8]} "
            f"{formatted_number[8:12]} {formatted_number[12:]}"
        )
