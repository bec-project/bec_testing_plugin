"""Example macros in a nested namespace: this file is available as `bec.macros.alignment.y`."""


def align_y(start: float = -1.0, stop: float = 1.0, steps: int = 11) -> dict[str, float | int]:
    """Pretend to align the sample in y."""
    print(f"Aligning y from {start} to {stop} in {steps} steps...")
    return {"start": start, "stop": stop, "steps": steps}
