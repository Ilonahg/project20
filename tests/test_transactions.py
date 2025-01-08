# tests/test_transactions.py
import pytest
from generators.transactions import filter_by_currency, transaction_descriptions, card_number_generator

# Тест для filter_by_currency
def test_filter_by_currency():
    transactions = [
        {
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Перевод организации"
        },
        {
            "operationAmount": {
                "currency": {"code": "RUB"}
            },
            "description": "Перевод с карты на карту"
        }
    ]
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]['operationAmount']['currency']['code'] == "USD"

def test_empty_filter_by_currency():
    transactions = []
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 0

# Тест для transaction_descriptions
def test_transaction_descriptions():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"}
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Перевод организации", "Перевод с карты на карту"]

# Тест для card_number_generator
@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']),
    (5, 7, ['0000 0000 0000 0005', '0000 0000 0000 0006', '0000 0000 0000 0007'])
])
def test_card_number_generator(start, stop, expected):
    generated = list(card_number_generator(start, stop))
    assert generated == expected
