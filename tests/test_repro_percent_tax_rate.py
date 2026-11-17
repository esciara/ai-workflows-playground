import pytest

from minicart.cart import Cart


def test_percent_tax_rate_raises_value_error():
    with pytest.raises(ValueError, match="between 0 and 1"):
        Cart(tax_rate='8%')


def test_nan_tax_rate_raises_value_error():
    with pytest.raises(ValueError, match="between 0 and 1"):
        Cart(tax_rate='nan')
