import pytest

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def test_freezing_point():
    # 0°C should be 32°F
    assert celsius_to_fahrenheit(0) == 32

def test_boiling_point():
    # 100°C should be 212°F
    assert celsius_to_fahrenheit(100) == 212

def test_negative_temperature():
    # -40°C should be -40°F (special case where both scales meet)
    assert celsius_to_fahrenheit(-40) == -40
