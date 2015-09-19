#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module will convert Fahrenheit to Celsius."""


from decimal import Decimal

ABSOLUTE_DIFFERENCE = Decimal('273.15')

def fahrenheit_to_celsius(degrees):
    """This will change the degrees to C from F.

    Args:
        degrees(int):the temperature in degrees F.

    Returns:
        decimal: decimal representation in degrees C.

    Examples:
        fahrenheit_to_celsius(212)
        'Decimal (100.0)'
    """
    return 'Decimal ({})'.format((5.0000*((degrees)-32.0000))/9.0000, '.3f')

def celsius_to_kelvin(degrees):
    """This will change the degrees to K from C.

    Args:
        degrees(decimal):the temperature in degrees C(decimal form).

    Returns:
        decimal: decimal representation in degrees K.

    Examples:
        celsius_to_kelvin(212)
        'Decimal (100.0)'
    """
    return 'Decimal ({})'.format(ABSOLUTE_DIFFERENCE+degrees, '.3f')
