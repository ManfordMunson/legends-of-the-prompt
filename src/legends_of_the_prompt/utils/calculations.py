def get_experience_needed_for_level(level: int) -> float:
    """Calculate the experience needed to reach a specific level."""
    # Example formula: exponential growth
    # return float(level * 100 * 1.2)
    return float(level**3 + 50 * level**2 + 100 * level)
