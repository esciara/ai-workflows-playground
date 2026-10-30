from decimal import Decimal

import pytest

from minicart.money import round_money, to_decimal


@pytest.mark.parametrize(
    "raw, expected",
    [("1.005", "1.01"), ("1.004", "1.00"), (2, "2.00"), (0.1, "0.10"), ("-1.005", "-1.01")],
)
def test_round_money(raw, expected):
    assert round_money(raw) == Decimal(expected)


def test_to_decimal_avoids_float_artefacts():
    assert to_decimal(0.1) == Decimal("0.1")
