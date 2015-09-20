#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a docstring"""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Takes fahrenheit and converts it to celsius.

    This function takes a number (fahrenheit) and converts it into celcius.

    Args:
        degrees (mixed): A number representing degrees in Fahrenheit

    Returns:
        celsius (mixed): The celcius dgrees representation of the Fahrenheit

    Example:
        >>> fahrenheit_to_celsius(98.7)
        Decimal('37.0555555555555571345394128')

    """
    degrees = decimal.Decimal(str(degrees))
    #celsius = decimal.Decimal(str(round(((degrees - 32) * 5) / 9, 2)))
    celsius = ((degrees - 32) * 5) / 9
    return celsius


def celsius_to_kelvin(degrees):
    """Takes celsius and converts it to kelvin.

    This function takes a number (fahrenheit) and converts it into celcius.

    Args:
        degrees (mixed): A number representing degrees in celsius

    Returns:
        kelvin (mixed): The kelvin degrees representation of the celsius

    Example:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')

    """
    degrees = decimal.Decimal(str(degrees))
    kelvin = degrees + ABSOLUTE_DIFFERENCE
    return kelvin


def fahrenheit_to_kelvin(degrees):
    """Takes fahrenheit and converts it to kelvin.

    This function takes a number (fahrenheit) and converts it into kelvin.

    Args:
        degrees (mixed): A number representing degrees in fahrenheit

    Returns:
        kelvin (mixed): The kelvin degrees representation of the fahrenheit

    Example:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')

    """
    celval = fahrenheit_to_celsius(degrees)
    kelval = celsius_to_kelvin(celval)
    return kelval
