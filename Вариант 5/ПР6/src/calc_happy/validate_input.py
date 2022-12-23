def validate_input(inp):
    try:
        validated = int(inp)
        if validated <= 0:
            raise ValueError
    except ValueError:
        print("Incorrect value (n must be int, n must be > 0)")
        return False

    return validated
