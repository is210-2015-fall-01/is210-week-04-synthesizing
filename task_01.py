#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides calculation temparature """


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal(273.15)


def fahrenheit_to_celsius(degrees):
    """ This function will convert fahrenheit to celsius."""

    return (decimal.Decimal(degrees) -32) *5 /9


def celsius_to_kelvin(degrees):
    """ This function convert celsius to kelvin"""

    return decimal.Decimal(degrees)+ ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """This function convert fahrenheit to kelvin"""

    # return celsius_to_kelvin( fahrenheit_to_celsius() )
    celsius = fahrenheit_to_celsius(degrees)
    kelvin = celsius_to_kelvin(celsius)

    return kelvin
