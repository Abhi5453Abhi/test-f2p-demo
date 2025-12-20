"""Unit conversion module for temperature, length, weight, and volume."""

from typing import Dict, List
from enum import Enum


class TemperatureUnit(Enum):
    """Temperature unit types."""
    CELSIUS = "celsius"
    FAHRENHEIT = "fahrenheit"
    KELVIN = "kelvin"


class LengthUnit(Enum):
    """Length unit types."""
    METER = "meter"
    KILOMETER = "kilometer"
    CENTIMETER = "centimeter"
    MILLIMETER = "millimeter"
    MILE = "mile"
    FOOT = "foot"
    INCH = "inch"
    YARD = "yard"


class WeightUnit(Enum):
    """Weight unit types."""
    KILOGRAM = "kilogram"
    GRAM = "gram"
    POUND = "pound"
    OUNCE = "ounce"
    TON = "ton"
    STONE = "stone"


class VolumeUnit(Enum):
    """Volume unit types."""
    LITER = "liter"
    MILLILITER = "milliliter"
    GALLON = "gallon"
    QUART = "quart"
    PINT = "pint"
    CUP = "cup"
    FLUID_OUNCE = "fluid_ounce"
    CUBIC_METER = "cubic_meter"


# Temperature Conversions
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Convert Fahrenheit to Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Convert Kelvin to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between different units.
    
    Args:
        value: Temperature value to convert
        from_unit: Source unit (celsius, fahrenheit, kelvin)
        to_unit: Target unit (celsius, fahrenheit, kelvin)
    
    Returns:
        Converted temperature value
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit == to_unit:
        return value
    
    # Convert to Celsius first
    if from_unit == "celsius" or from_unit == "c":
        celsius = value
    elif from_unit == "fahrenheit" or from_unit == "f":
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == "kelvin" or from_unit == "k":
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")
    
    # Convert from Celsius to target
    if to_unit == "celsius" or to_unit == "c":
        return celsius
    elif to_unit == "fahrenheit" or to_unit == "f":
        return celsius_to_fahrenheit(celsius)
    elif to_unit == "kelvin" or to_unit == "k":
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")


# Length Conversions (all to meters as base)
_LENGTH_TO_METERS: Dict[str, float] = {
    "meter": 1.0,
    "kilometer": 1000.0,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "mile": 1609.344,
    "foot": 0.3048,
    "inch": 0.0254,
    "yard": 0.9144,
}


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """Convert length between different units.
    
    Args:
        value: Length value to convert
        from_unit: Source unit (meter, kilometer, centimeter, millimeter, mile, foot, inch, yard)
        to_unit: Target unit (meter, kilometer, centimeter, millimeter, mile, foot, inch, yard)
    
    Returns:
        Converted length value
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    # Handle aliases
    unit_aliases = {
        "m": "meter", "km": "kilometer", "cm": "centimeter", "mm": "millimeter",
        "mi": "mile", "ft": "foot", "in": "inch", "yd": "yard"
    }
    from_unit = unit_aliases.get(from_unit, from_unit)
    to_unit = unit_aliases.get(to_unit, to_unit)
    
    if from_unit not in _LENGTH_TO_METERS:
        raise ValueError(f"Unknown length unit: {from_unit}")
    if to_unit not in _LENGTH_TO_METERS:
        raise ValueError(f"Unknown length unit: {to_unit}")
    
    if from_unit == to_unit:
        return value
    
    meters = value * _LENGTH_TO_METERS[from_unit]
    return meters / _LENGTH_TO_METERS[to_unit]


# Weight Conversions (all to kilograms as base)
_WEIGHT_TO_KILOGRAMS: Dict[str, float] = {
    "kilogram": 1.0,
    "gram": 0.001,
    "pound": 0.453592,
    "ounce": 0.0283495,
    "ton": 1000.0,
    "stone": 6.35029,
}


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    """Convert weight between different units.
    
    Args:
        value: Weight value to convert
        from_unit: Source unit (kilogram, gram, pound, ounce, ton, stone)
        to_unit: Target unit (kilogram, gram, pound, ounce, ton, stone)
    
    Returns:
        Converted weight value
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    # Handle aliases
    unit_aliases = {
        "kg": "kilogram", "g": "gram", "lb": "pound", "lbs": "pound",
        "oz": "ounce", "t": "ton", "st": "stone"
    }
    from_unit = unit_aliases.get(from_unit, from_unit)
    to_unit = unit_aliases.get(to_unit, to_unit)
    
    if from_unit not in _WEIGHT_TO_KILOGRAMS:
        raise ValueError(f"Unknown weight unit: {from_unit}")
    if to_unit not in _WEIGHT_TO_KILOGRAMS:
        raise ValueError(f"Unknown weight unit: {to_unit}")
    
    if from_unit == to_unit:
        return value
    
    kilograms = value * _WEIGHT_TO_KILOGRAMS[from_unit]
    return kilograms / _WEIGHT_TO_KILOGRAMS[to_unit]


# Volume Conversions (all to liters as base)
_VOLUME_TO_LITERS: Dict[str, float] = {
    "liter": 1.0,
    "milliliter": 0.001,
    "gallon": 3.78541,
    "quart": 0.946353,
    "pint": 0.473176,
    "cup": 0.236588,
    "fluid_ounce": 0.0295735,
    "cubic_meter": 1000.0,
}


def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    """Convert volume between different units.
    
    Args:
        value: Volume value to convert
        from_unit: Source unit (liter, milliliter, gallon, quart, pint, cup, fluid_ounce, cubic_meter)
        to_unit: Target unit (liter, milliliter, gallon, quart, pint, cup, fluid_ounce, cubic_meter)
    
    Returns:
        Converted volume value
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    # Handle aliases
    unit_aliases = {
        "l": "liter", "ml": "milliliter", "gal": "gallon", "qt": "quart",
        "pt": "pint", "c": "cup", "fl_oz": "fluid_ounce", "floz": "fluid_ounce",
        "m3": "cubic_meter", "cubic_m": "cubic_meter"
    }
    from_unit = unit_aliases.get(from_unit, from_unit)
    to_unit = unit_aliases.get(to_unit, to_unit)
    
    if from_unit not in _VOLUME_TO_LITERS:
        raise ValueError(f"Unknown volume unit: {from_unit}")
    if to_unit not in _VOLUME_TO_LITERS:
        raise ValueError(f"Unknown volume unit: {to_unit}")
    
    if from_unit == to_unit:
        return value
    
    liters = value * _VOLUME_TO_LITERS[from_unit]
    return liters / _VOLUME_TO_LITERS[to_unit]


def get_available_units(category: str) -> List[str]:
    """Get list of available units for a given category.
    
    Args:
        category: Unit category (temperature, length, weight, volume)
    
    Returns:
        List of available unit names
    """
    category = category.lower()
    
    if category == "temperature":
        return ["celsius", "fahrenheit", "kelvin"]
    elif category == "length":
        return list(_LENGTH_TO_METERS.keys())
    elif category == "weight":
        return list(_WEIGHT_TO_KILOGRAMS.keys())
    elif category == "volume":
        return list(_VOLUME_TO_LITERS.keys())
    else:
        raise ValueError(f"Unknown category: {category}. Must be one of: temperature, length, weight, volume")

