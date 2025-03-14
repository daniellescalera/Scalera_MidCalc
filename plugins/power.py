"""Power function plugin"""

def power(base: float, exponent: float) -> float:
    """Returns base raised to the power of exponent."""
    return base ** exponent

def plugin_info():
    """Returns plugin command and function reference."""
    return {
        "command": "power",
        "function": power,
        "description": "Calculate base raised to the power of exponent."
    }
