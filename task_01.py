#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task01"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Docstring explaining what degrees mean.

    Args:
        degrees (int): Arg to be converted to celsius.

    Returns:
         (dec): Argument returns celius in decimal format.

    Examples:
        >>>fahrenheit_to_celsius(275)
        Decimal('135')

        fahrenheit_to_celsius(212)
        Decimal('100')
    """
    celsius = ((degrees - 32) * 5) / decimal.Decimal('9')
    return celsius


def celsius_to_kelvin(degrees):
    """Docstring explaining what degrees mean.

    Args:
        degrees (int): Arg to be converted to kelvin.

    Returns:
         (dec): Argument returns kelvin in decimal format.

    Examples:
        >>>celsius_to_kelvin(100)
        Decimal('375.15')

    """
    kelvin = ABSOLUTE_DIFFERENCE + degrees
    return decimal.Decimal(kelvin)


def fahrenheit_to_kelvin(degrees):
    """Docstring explaining what degrees mean.

    Args:
        degrees (int): Arg to be converted to kelvin from fahrenheit.

    Returns:
         (dec): Argument returns kelvin in decimal format.

    Examples:
        >>>fahrenheit_to_kelvin(212)
        Decimal('373.15')
    """
    kelvin = (celsius_to_kelvin(fahrenheit_to_celsius(degrees)))
    return decimal.Decimal(kelvin)
