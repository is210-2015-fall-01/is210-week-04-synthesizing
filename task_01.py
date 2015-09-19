#!user/bin/env python
# -*- coding: utf-8 -*-
"""Module that converts fahrenheit to celsius"""

import decimal

def fahrenheit_to_celsius(degrees=decimal.Decimal('53')):
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
    return (str(degrees - a) * b / c)


print fahrenheit_to_celsius()






