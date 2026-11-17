from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def to_decimal(value: Decimal | int | float | str) -> Decimal:
    """Convert a number to Decimal without float artefacts."""
    if isinstance(value, Decimal):
        return value
    try:
        return Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f"invalid number: {value!r}") from exc


def round_money(value: Decimal | int | float | str) -> Decimal:
    """Round to cents, half up (0.005 -> 0.01)."""
    return to_decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
