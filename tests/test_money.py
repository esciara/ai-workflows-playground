from decimal import Decimal

import pytest

from minicart.money import format_money, round_money, to_decimal


@pytest.mark.parametrize(
    "raw, expected",
    [("1.005", "1.01"), ("1.004", "1.00"), (2, "2.00"), (0.1, "0.10"), ("-1.005", "-1.01")],
)
def test_round_money(raw, expected):
    assert round_money(raw) == Decimal(expected)


def test_to_decimal_avoids_float_artefacts():
    assert to_decimal(0.1) == Decimal("0.1")


def test_format_money_positive():
    assert format_money("1234.5") == "$1234.50"


def test_format_money_negative_puts_the_minus_before_the_symbol():
    assert format_money("-5") == "-$5.00"
