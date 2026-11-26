from decimal import Decimal, ROUND_HALF_UP


def to_decimal(value: Decimal | int | float | str) -> Decimal:
    """Convert a numbr to Decimal without flaot artefacts."""
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def round_money(value: Decimal | int | float | str) -> Decimal:
    """Round to cents, half up (0.005 -> 0.01)."""
    return to_decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def format_money(value: Decimal | int | float | str) -> str:
    """Format an amount for display, e.g. 1234.5 -> '$1234.50'."""
    amount = round_money(value)
    sign = "-" if amount < 0 else ""
    return f"{sign}${abs(amount)}"
