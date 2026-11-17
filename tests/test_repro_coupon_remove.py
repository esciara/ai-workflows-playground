from decimal import Decimal

from minicart.cart import Cart
from minicart.discounts import apply_coupon


def test_coupon_dropped_when_subtotal_below_minimum_after_remove():
    cart = Cart()
    cart.add("A", "15.00")
    cart.add("B", "10.00")
    apply_coupon(cart, "FIVEOFF")
    cart.remove("B")
    assert cart.total() == Decimal("15.00")


def test_percent_coupon_follows_added_items():
    cart = Cart()
    cart.add("A", "100.00")
    apply_coupon(cart, "SAVE10")
    cart.add("B", "100.00")
    assert cart.total() == Decimal("180.00")
