"""Bulk pricing (e2e fork PR seed)."""

from decimal import Decimal


def bulk_price(unit: Decimal, qty: int, percent_off: Decimal) -> Decimal:
    """Total for `qty` units at `unit` each, with `percent_off` % off."""
    return unit * qty * (1 - percent_off)
