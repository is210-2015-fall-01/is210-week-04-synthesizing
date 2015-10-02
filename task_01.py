#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module will convert Fahrenheit to Celsius.
There is also a conversion from C to K and F directly to K."""

import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """This will change the degrees to Celsius from Fahrenheit.

    Args:
        degrees(int):the temperature in degrees F.

    Returns:
        decimal: decimal representation in degrees C.

    Examples:

        >>>fahrenheit_to_celsius(212)
        Decimal ('100.0')
    """
    return (5*(decimal.Decimal(degrees)-32))/9


def celsius_to_kelvin(degrees):
    """This will change the degrees to Kelvin from Celsius.

    Args:
        degrees(decimal):the temperature in degrees C.

    Returns:
        decimal: decimal representation of temperature in degrees K.

    Examples:

        >>>celsius_to_kelvin(100)
        Decimal ('373.15')
        >>>celsius_to_kelvin(200)
        Decimal ('473.15')
    """
    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):

    """This will change the degrees to Kelvin from Fahrenheit.

    Args:
        degrees(decimal):the temperature in degrees in F.

    Returns:
        decimal: decimal representation in degrees K.

    Examples:

        >>>fahrenheit_to_kelvin(212)
        Decimal ('373.15')
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
