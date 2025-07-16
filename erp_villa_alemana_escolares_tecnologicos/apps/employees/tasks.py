from numba import njit


@njit(looplift=True, fastmath=True, nopython=True)
def validate_rut(rut: str) -> bool:
    """
    Validate a Chilean RUT (Rol Único Tributario).

    Args:
        rut (str): The RUT to validate.

    Returns:
        bool: True if the RUT is valid, False otherwise.
    """
    if not rut or len(rut) < 2:
        return False

    # Extract the numeric part and the verification digit
    numeric_part = rut[:-1]
    verification_digit = rut[-1].upper()

    # Validate numeric part
    if not numeric_part.isdigit():
        return False

    # Calculate the expected verification digit
    total = 0
    factor = 2
    for digit in reversed(numeric_part):
        total += int(digit) * factor
        factor = 9 if factor == 7 else factor + 1

    remainder = total % 11
    expected_digit = "K" if remainder == 10 else str(11 - remainder)

    return expected_digit == verification_digit
