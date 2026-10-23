"""Example macros in a nested namespace: this file is available as `bec.macros.alignment.x`."""


def align_x(start: float = -1.0, stop: float = 1.0, steps: int = 11) -> dict[str, float | int]:
    """Pretend to align the sample in x."""
    print(f"Aligning x from {start} to {stop} in {steps} steps...")
    return {"start": start, "stop": stop, "steps": steps}
