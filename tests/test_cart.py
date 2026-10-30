from decimal import Decimal

import pytest

from minicart import Cart


def test_empty_cart_totals_are_zero():
    cart = Cart()
    assert cart.subtotal() == Decimal("0.00")
    assert cart.total() == Decimal("0.00")
    assert cart.item_count() == 0


def test_add_and_subtotal():
    cart = Cart()
    cart.add("apple", "0.50", 3)
    cart.add("pear", "1.25")
    assert cart.subtotal() == Decimal("2.75")
    assert cart.item_count() == 4


def test_add_same_sku_merges_quantity():
    cart = Cart()
    cart.add("apple", "0.50", 2)
    cart.add("apple", "0.50", 3)
    assert len(cart.items) == 1
    assert cart.items[0].quantity == 5


def test_add_same_sku_different_price_rejected():
    cart = Cart()
    cart.add("apple", "0.50")
    with pytest.raises(ValueError):
        cart.add("apple", "0.60")


@pytest.mark.parametrize("qty", [0, -1])
def test_add_rejects_non_positive_quantity(qty):
    with pytest.raises(ValueError):
        Cart().add("apple", "1", qty)


def test_add_rejects_negative_price_and_empty_sku():
    with pytest.raises(ValueError):
        Cart().add("apple", "-1")
    with pytest.raises(ValueError):
        Cart().add("", "1")


def test_remove_partial_and_full():
    cart = Cart()
    cart.add("apple", "1", 5)
    cart.remove("apple", 2)
    assert cart.item_count() == 3
    cart.remove("apple")
    assert cart.items == []


def test_remove_unknown_sku_raises():
    with pytest.raises(KeyError):
        Cart().remove("ghost")


def test_tax_and_total():
    cart = Cart(tax_rate="0.20")
    cart.add("book", "10.00", 2)
    assert cart.tax() == Decimal("4.00")
    assert cart.total() == Decimal("24.00")


def test_tax_rounding_half_up():
    cart = Cart(tax_rate="0.075")
    cart.add("pen", "0.10")
    assert cart.tax() == Decimal("0.01")


@pytest.mark.parametrize("rate", ["-0.1", "1.5"])
def test_invalid_tax_rate(rate):
    with pytest.raises(ValueError):
        Cart(tax_rate=rate)


def test_clear_resets_items_and_discount():
    cart = Cart()
    cart.add("apple", "1")
    cart.discount = Decimal("0.5")
    cart.clear()
    assert cart.items == []
    assert cart.discount == Decimal("0")
