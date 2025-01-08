# Модуль генераторов

Этот модуль включает функции и генераторы для обработки данных транзакций.

## filter_by_currency

Функция фильтрует транзакции по валюте.

Пример использования:

```python
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
