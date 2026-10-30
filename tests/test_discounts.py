from decimal import Decimal

import pytest

from minicart import Cart, CouponError, apply_coupon


def make_cart(amount: str, tax_rate: str = "0") -> Cart:
    cart = Cart(tax_rate=tax_rate)
    cart.add("thing", amount)
    return cart


def test_percent_coupon():
    cart = make_cart("50.00")
    assert apply_coupon(cart, "SAVE10") == Decimal("5.00")
    assert cart.total() == Decimal("45.00")


def test_coupon_code_is_case_insensitive_and_trimmed():
    cart = make_cart("50.00")
    assert apply_coupon(cart, "  save10 ") == Decimal("5.00")


def test_fixed_coupon_applies_above_minimum():
    cart = make_cart("20.00")
    assert apply_coupon(cart, "FIVEOFF") == Decimal("5")
    assert cart.total() == Decimal("15.00")


def test_fixed_coupon_below_minimum_rejected():
    with pytest.raises(CouponError):
        apply_coupon(make_cart("19.99"), "FIVEOFF")


def test_unknown_coupon_rejected():
    with pytest.raises(CouponError):
        apply_coupon(make_cart("10"), "NOPE")


def test_discount_is_applied_before_tax():
    cart = make_cart("100.00", tax_rate="0.10")
    apply_coupon(cart, "HALF")
    assert cart.tax() == Decimal("5.00")
    assert cart.total() == Decimal("55.00")


def test_new_coupon_replaces_previous_one():
    cart = make_cart("100.00")
    apply_coupon(cart, "HALF")
    apply_coupon(cart, "SAVE10")
    assert cart.discount == Decimal("10.00")
