#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converting a Fahrenheit temperature to Kelvin task 1-3."""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """A function to convert fahrenheit to celsius.

    The input will be converted from fahrenheit to celcious and returned
    as a decimal.

    Args:
       degrees (int): A value in fahrenheit.
    Returns:
        Returns the temperature in celsius as a decimal.
    Example:

    >>> fahrenheit_to_celsius(212)
     Decimal('100')

    """
    return ((decimal.Decimal(degrees) - 32) * 5) / 9


def celsius_to_kelvin(degrees):
    """Performs arithmetic to convert temperature from celsius to kelvin.
    Args:
        degrees (int): Arg to be added to ABSOLUTE DIFFERENCE.
    Returns:
        int: Arg converted to another value arithmetically.
    Examples:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')
        >>> celsius_to_kelvin(50)
        Decimal('323.15')
    """
    return degrees + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """Performs arithmetic to convert temperature from fahrenheit to kelvin.
    Args:
        degrees (int): Arg to be converted another in through arithmetic, then
        converted again by adding to ABSOLUTE_DIFFERENCE.
    Returns:
        int: Arg converted to another value arithmetically.
    Examples:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
        >>> fahrenheit_to_kelvin(72)
        Decimal('295.3722222222222222222222222')
    """

    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
