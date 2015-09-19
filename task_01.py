#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module will convert Fahrenheit to Celsius."""


def fahrenheit_to_celsius(degrees):
    """This will change the degrees to C from F.

    Args:
        degrees(float):the temperature in degrees F.

    Returns:
        decimal: decimal representation in degrees C.

    Examples:
        fahrenheit_to_celsius(212)
        'Decimal (100.0)'
    """
    return 'Decimal ({})'.format((5.0000*((degrees * 1.0000)-32.0000))/9.0000, '.3f')
