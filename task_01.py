#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A more complex case of using multiple functions."""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Convert the degrees Fahrenheit to Celsius
    Args:
        degress: Fahrenheit to a decimal representation of degrees Celsius

    Returns:
            Return the temperature as a decimal in degrees Celsius.
    """
    return ((decimal.Decimal(degrees) - 32) * 5) / 9


def celsius_to_kelvin(degrees):
    """Converts from Celsius to Kelvin.
    Args:
        degress: Convert the degrees Celsius to degrees Kelvin

    Returns:
            Return the temperature as a decimal in degrees Kelvin.
    """
    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """Converting a Fahrenheit temperature to Kelvin.
    Args:
        degress: Convert Fahrenheit temperatures to Kelvin

    Returns:
             Return the result as a number.
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
