from decimal import Decimal

from minicart.money import round_money

# code -> (kind, value, minimum subtotal)
COUPONS: dict[str, tuple[str, Decimal, Decimal]] = {
    "SAVE10": ("percent", Decimal("10"), Decimal("0")),
    "FIVEOFF": ("fixed", Decimal("5"), Decimal("20")),
    "HALF": ("percent", Decimal("50"), Decimal("100")),
}


def compute_discount(code: str, subtotal: Decimal) -> Decimal | None:
    """Discount for a coupon at a subtotal, or None if below its minimum."""
    kind, value, minimum = COUPONS[code]
    if subtotal < minimum:
        return None
    if kind == "percent":
        return round_money(subtotal * value / 100)
    return min(value, subtotal)
