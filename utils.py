from typing import Any


def sorted_(data):
    """
    Выводит (EXECUTED) операции,
    сверху списка находятся самые последние операции (по дате).
    """
    items = [i for i in data if i.get("state") == "EXECUTED"]
    items.sort(key=lambda x: x.get("date"), reverse=True)
    return items


def prepare_msg(item: dict[str, Any]):
    """
    Выводит список в формате
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    """
    date = get_date(item.get("date"))
    description = item.get("description")
    from_ = mask_from_to(item.get("from"))
    to_ = mask_from_to(item.get("to"))
    amount = item.get("operationAmount").get("amount")
    currency = item.get("operationAmount").get("currency").get("name")

    if from_:
        from_ += ' ->'
    else:
        from_ = ''

    return f"{date} {description}\n{from_} {to_}\n{amount} {currency}"


def get_date(date):
    """
    Выводит дату в формате
    ДД.ММ.ГГГГ (пример: 14.10.2018).
    """
    date_raw = date[0:10].split(sep="-")
    return f"{date_raw[2]}.{date_raw[1]}.{date_raw[0]}"


def mask_from_to(number):
    """
    Переводит номер счета из формата "Счет 56363465303962313778"
    в формат "Счет **3778"
    и номер карты из формата "MasterCard 8826230888662405"
    в формат "MasterCard 8826 23** **** 2405"
    """
    if number is None:
        return ""

    msg = number.split()

    if msg[0] == "Счет":
        number_hidden = mask_account(msg[-1])
    else:
        number_hidden = mask_card_number(msg[-1])

    return ' '.join(msg[:-1]) + ' ' + number_hidden


def mask_account(number):
    """
    Выводит номер счета в формате
    **XXXX
    (видны только последние 4 цифры номера счета)
    """
    if number.isdigit() and len(number) > 4:
        return f"**{number[-4:]}"


def mask_card_number(number: str):
    """
    Выводит номер карты в формате
    XXXX XX** **** XXXX (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом).
    """
    if number.isdigit() and len(number) == 16:
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
