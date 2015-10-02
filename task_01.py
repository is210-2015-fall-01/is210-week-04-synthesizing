#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Complex case of using mutiple function."""


from decimal import Decimal

ABSOLUTE_DIFFERENCE = Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Created a function with one parameter, to convert fahrenheit to celsius.

    Args:
       degrees(mixed): A number that will be used in temperature coversion
       operation.

    Returns:
        str: Temperature after conversion from fahrenheit to celsius after
             the conversion formula has been executed.

    Example:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')
    """
    return(Decimal(degrees)-32)*5/9


def celsius_to_kelvin(degrees):
    """Created a function, with one parameter, to convert celsius into kelvin.

    Args:
        degrees(mixed): A number that will be used in temperature conversion
        operation.

    Returns:
        str: Temperature after conversion from celsius to kelvin.

    Example:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')
    """
    return degrees + ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """Created a function, with one parameter, to convert fahrenheit to kelvin.

    Args:
       degrees(mixed): A number that will be used in temperature coversion
       operation.

    Returns:
        str: Temperature after conversion from fahrenheit to kelvin.

    Example:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
    """
    return fahrenheit_to_celsius(degrees) + ABSOLUTE_DIFFERENCE
