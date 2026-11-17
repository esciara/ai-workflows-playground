from decimal import Decimal

from minicart.cart import Cart
from minicart.coupons import COUPONS, compute_discount  # noqa: F401

class CouponError(ValueError):
    pass


def apply_coupon(cart: Cart, code: str) -> Decimal:
    """Apply a coupon to the cart; return the discount amount. Codes are case-insensitive."""
    key = code.strip().upper()
    if key not in COUPONS:
        raise CouponError(f"unknown coupon: {code}")
    discount = compute_discount(key, cart.subtotal())
    if discount is None:
        raise CouponError(f"{key} needs a subtotal of at least {COUPONS[key][2]}")
    cart.coupon = key
    cart.discount = discount
    return discount
