"""Example macros two levels deep: this file is available as `bec.macros.alignment.fine.center_beam`."""


def center_beam(tolerance: float = 0.01) -> float:
    """Pretend to center the beam to within the given tolerance."""
    print(f"Centering the beam to within {tolerance}...")
    return tolerance
