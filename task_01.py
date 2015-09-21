#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Temperature Coversion Calculators"""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Function that converts fahrenheit to celcisus.

    Args:
        degrees(int): Input fahrenheit to be converted

    Returns:
        decimal: Farenheit is converted to celsius.

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> fahrenheit_to_celsius(-40)
        Decimal('-40')
    """
    conversion_c = (((decimal.Decimal(degrees) - 32) * 5) / 9)
    return conversion_c


def celsius_to_kelvin(degrees):
    """Function that converts celsius to kelvin.

    Args:
        degrees(int): Input celsius to be converted.

    Returns:
        decimal: Celcius is converted to kelvin.

    Examples:

        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> celsius_to_kelvin(50)
        Decimal('323.15')
    """
    conversion_k = degrees + ABSOLUTE_DIFFERENCE
    return conversion_k


def fahrenheit_to_kelvin(degrees):
    """Function that converts fahrenheit to kelvin.

    Args:
        degrees(int): Input fahrenheit to be converted.

    Returns:
        decimal: Fahrenheit is converted to kelvin.

    Examples:

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')

        >>> fahrenheit_to_kelvin(59)
        Decimal('288.15')
    """
    conversion_fk = celsius_to_kelvin(fahrenheit_to_celsius(degrees))
    return conversion_fk
