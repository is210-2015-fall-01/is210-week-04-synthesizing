#!user/bin/env python
# -*- coding: utf-8 -*-
"""Module that converts fahrenheit to celsius"""


import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Does math to return conversion from f to c as a decimal.

    Args:
        degrees (dec): degree to be converted.

    Returns:
        (dec) converted to celsius.

    Examples:
        fahrenheit_to_celsius(53)
        >>>> '11.66666666666666666666666667'
    """
    deg_far = decimal.Decimal(degrees)
    val_a = decimal.Decimal('32')
    val_b = decimal.Decimal('5')
    val_c = decimal.Decimal('9')

    dec_val = ((deg_far - val_a) * val_b) / val_c

    return dec_val


def celsius_to_kelvin(degrees):
    """"Does math to convert celsius to kelvin.

    Args:
        degrees (dec): degree in celsius to be converted.

    Returns:
        (dec) converted to kelvin.

    Examples:
        celsius_to_kelvin(100)
        >>> '373.15'
    """
    deg_cel = decimal.Decimal(degrees)
    val_kelv = deg_cel + ABSOLUTE_DIFFERENCE

    return val_kelv


print celsius_to_kelvin(100)

print fahrenheit_to_celsius(53)
