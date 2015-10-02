#!user/bin/env python
# -*- coding: utf-8 -*-
"""Module that converts degrees in either fahrenheit or celsius into
   either celsius or kelvin"""


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


def fahrenheit_to_kelvin(degrees):
    """Does math to combine the above two functions in order to
       convert fahrenheit to kelvin.

    Args:
        degrees (dec): degree en fahrenheit to be converted

    Returns:
        (dec) converted to kelvin

    Examples:
        fahrenheit_to_kelvin(53)
        >>> '284.8166666666666666666666667'
    """
    dec = decimal.Decimal(degrees)
    f_to_c = fahrenheit_to_celsius(dec)
    c_to_k = celsius_to_kelvin(f_to_c)

    return c_to_k


print fahrenheit_to_celsius(53)
print celsius_to_kelvin(100)
print fahrenheit_to_kelvin(53)
