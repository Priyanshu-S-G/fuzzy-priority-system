def defuzzify(aggregated: dict) -> float:
    """
    Convert aggregated fuzzy set to single crisp output score.

    Intended behavior:
        Apply Centroid of Area (CoA) method over output universe [0, 100].
        Integrate the aggregated membership function and compute centroid.

    Args:
        aggregated: dict from aggregate()

    Returns:
        float crisp score in range [0, 100]
    """
    # TODO: Replace with real centroid calculation
    # Dummy: weighted average of representative crisp values per set
    set_centers = {"low": 20.0, "medium": 50.0, "high": 80.0}
    weights = sum(aggregated.values())
    if weights == 0:
        return 50.0
    score = sum(aggregated[s] * set_centers[s] for s in aggregated) / weights
    return round(score, 2)