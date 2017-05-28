"""Implementation of permutations.

This uses the "interleaving" technique, which I find the most intuitive. It's
not the most efficient algorithm.
"""


def interleave(x, xs):
    """Interleave x into xs."""
    for pos in range(len(xs) + 1):
        yield xs[:pos] + [x] + xs[pos:]


def permutations(xs):
    """Generate the permuations of xs."""
    if len(xs) == 0:
        yield []
    else:
        for subperm in permutations(xs[1:]):
            for inter in interleave(xs[0], subperm):
                yield inter


def list_permutations(xs):
    """Permutations as a list."""
    return list(permutations(xs))
