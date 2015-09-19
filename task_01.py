#!user/bin/env python
# -*- coding: utf-8 -*-
"""Module that tests to see if there are enough litterboxes"""

import decimal

def fahrenheit_to_celsius(degrees):
    """ Returns two integers and boolean to ensure that there enough litterboxes
        for all of the cats.

    Args:
        kittens (int): Number of kittens.
        litterboxes (int): Number of litterboxes.
        cafood (bool): At least some catfood? True or False.

    Returns:
        A bool value indicating whether or not there are enough litterboxes
        for all of the kittens and at least some catfood.

    Examples:
         too_many_kittens(4, 5, True)
    """
   
    degree_val = ((degrees - decimal.Decimal('32.0')) * decimal.Decimal('5') /
                  decimal.Decimal('9'))

    return degree_val

decimal1 = decimal.Decimal('95')

f_to_c = fahrenheit_to_celsius(decimal1)

print f_to_c
