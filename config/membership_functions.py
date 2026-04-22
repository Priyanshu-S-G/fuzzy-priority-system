def low(x, lo, mid):
    """
    Triangular MF: peak at lo, zero at mid
    """
    if x <= lo:
        return 1.0
    elif lo < x < mid:
        return (mid - x) / (mid - lo)
    else:
        return 0.0


def medium(x, lo, mid, hi):
    """
    Triangular MF: peak at mid
    """
    if lo < x < mid:
        return (x - lo) / (mid - lo)
    elif mid <= x < hi:
        return (hi - x) / (hi - mid)
    else:
        return 0.0


def high(x, mid, hi):
    """
    Triangular MF: zero at mid, peak at hi
    """
    if x >= hi:
        return 1.0
    elif mid < x < hi:
        return (x - mid) / (hi - mid)
    else:
        return 0.0