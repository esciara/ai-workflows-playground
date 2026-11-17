import pytest

from minicart.cart import Cart


def test_percent_tax_rate_raises_value_error():
    with pytest.raises(ValueError):
        Cart(tax_rate="8%")


def test_invalid_unit_price_raises_value_error():
    with pytest.raises(ValueError):
        Cart().add("a", "abc")
