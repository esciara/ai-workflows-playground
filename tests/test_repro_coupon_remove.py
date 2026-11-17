from decimal import Decimal

from minicart.cart import Cart
from minicart.discounts import apply_coupon


def test_coupon_dropped_when_subtotal_falls_below_minimum():
    cart = Cart()
    cart.add("A", "15.00")
    cart.add("B", "10.00")
    apply_coupon(cart, "FIVEOFF")
    cart.remove("B")
    assert cart.total() == Decimal("15.00")


def test_percent_coupon_follows_quantity_change():
    cart = Cart()
    cart.add("A", "10.00", 2)
    apply_coupon(cart, "SAVE10")
    cart.add("A", "10.00", 2)
    assert cart.discount == Decimal("4.00")
    cart.remove("A", 3)
    assert cart.discount == Decimal("1.00")
