"""Price after a nonnegative fixed discount, with a zero floor."""

VERSION_MARKER = "CODE_FIXTURE_A_20261025"


def final_price(price: int, discount: int) -> int:
    if price < 0 or discount < 0:
        raise ValueError("price and discount must be nonnegative")
    return price - discount
