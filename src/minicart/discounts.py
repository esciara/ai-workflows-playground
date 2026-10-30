from decimal import Decimal

from minicart.cart import Cart
from minicart.money import round_money

# code -> (kind, value, minimum subtotal)
COUPONS: dict[str, tuple[str, Decimal, Decimal]] = {
    "SAVE10": ("percent", Decimal("10"), Decimal("0")),
    "FIVEOFF": ("fixed", Decimal("5"), Decimal("20")),
    "HALF": ("percent", Decimal("50"), Decimal("100")),
}


class CouponError(ValueError):
    pass


def apply_coupon(cart: Cart, code: str) -> Decimal:
    """Apply a coupon to the cart; return the discount amount. Codes are case-insensitive."""
    key = code.strip().upper()
    if key not in COUPONS:
        raise CouponError(f"unknown coupon: {code}")
    kind, value, minimum = COUPONS[key]
    subtotal = cart.subtotal()
    if subtotal < minimum:
        raise CouponError(f"{key} needs a subtotal of at least {minimum}")
    if kind == "percent":
        discount = round_money(subtotal * value / 100)
    else:
        discount = min(value, subtotal)
    cart.discount = discount
    return discount
