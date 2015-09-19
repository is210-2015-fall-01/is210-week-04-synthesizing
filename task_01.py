#!user/bin/env python
# -*- coding: utf-8 -*-
"""Module that converts fahrenheit to celsius"""

import decimal

def fahrenheit_to_celsius(degrees):
    """ Returns conversion from f to c as a decimal.

    Args:
        kittens (dec): degree to be converted

    Returns:
        (dec) converted to celsius

    Examples:
         
    """

 

    a = decimal.Decimal('32')
    b = decimal.Decimal('5')
    c = decimal.Decimal('9')
    return ((degrees - a) * b / c)

DEGREE_VAL = decimal.Decimal('51')

print fahrenheit_to_celsius(DEGREE_VAL)






