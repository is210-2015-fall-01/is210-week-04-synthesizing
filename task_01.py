#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a module that contains 3 functions to convert temperature"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')

def celsius_to_kelvin(degrees):
    """This function converts celsius to kelvin.

    Args:
        degrees (mixed): Arg to be added to ABSOLULTE_DIFFERENCE

    Returns:
        int: the decimal value of Kelvin

    Example:

        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> celsius_to_kelvin(30.5)
        Decimal('303.65')
    """

    Kelvin = (ABSOLUTE_DIFFERENCE) + decimal.Decimal(degrees)

    return Kelvin

def fahrenheit_to_celsius(degrees):
    """This function converts fahrenheit to celsius.

    Args:
        degrees (mixed): Arg to be arithmetically incremented with a formula.

    Returns:
        int: the decimal value of Celsius.

    Exmaple:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> fahrenheit_to_celsius(150)
        Decimal('65.55555555555555555555555556')
    """
    Celsius = (decimal.Decimal(degrees) - 32) * 5 / 9

    return Celsius

def fahrenheit_to_kelvin(degrees):
    """This function converts fahrenheit_to_kelvin.  This function calls on two
    other functions: celsius_to_kelvin, fahrenheit_to_celsius.

    Args:
        degrees (mixed): Arg to be incremented with two other functions.

    Returns:
        int: The decimal value of Kelvin.

    Example:

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')

        >>> fahrenheit_to_kelvin(150.5)
        Decimal('338.9833333333333333333333333')
    """
    Celsius = fahrenheit_to_celsius(degrees)

    Kelvin = celsius_to_kelvin(Celsius)

    return Kelvin
