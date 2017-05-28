"""Implement powerset using the bit-testing technique."""


def nth_is_set(num, pos):
    return bool(num & (1 << pos))


def powerset(xs):
    """Generate the powerset of xs."""
    sz = len(xs)
    for x in range(1 << sz):
        yield [xs[i] for i in range(sz) if nth_is_set(x, i)]


def list_powerset(xs):
    return list(powerset(xs))
