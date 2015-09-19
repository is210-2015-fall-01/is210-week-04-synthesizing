#!user/bin/env python
# -*- coding: utf-8 -*-
"""Module that converts fahrenheit to celsius"""


import decimal


def fahrenheit_to_celsius(degrees):
    """ Returns conversion from f to c as a decimal.

    Args:
        degrees (dec): degree to be converted

    Returns:
        (dec) converted to celsius

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


print fahrenheit_to_celsius(53)
