def clamp(x, lo, hi):
    return max(lo, min(x, hi))


def normalize(x, lo, hi):
    return (x - lo) / (hi - lo)