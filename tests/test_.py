import pytest
from utils import (get_date, mask_from_to,
                   mask_account, mask_card_number)


def test_get_date():
    assert get_date("2019-07-13T18:51:29.313309") == "13.07.2019"


def test_mask_from_to():
    assert mask_from_to("Счет 56363465303962313778") == "Счет **3778"
    assert mask_from_to("Maestro 8602249654751155") == "Maestro 8602 24** **** 1155"
    assert mask_from_to("MasterCard 8826230888662405") == "MasterCard 8826 23** **** 2405"


def test_mask_account():
    assert mask_account("96119739109420349721") == "**9721"


def test_mask_card_number():
    assert mask_card_number("8826230888662405") == "8826 23** **** 2405"
