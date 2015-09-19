#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This function calculate temprature."""


from decimal import Decimal

ABSOLUTE_DIFFERENCE = Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """ This function will convert fahrenheit to celsius."""

    return (Decimal(degrees) -32)*5/9


def celsius_to_kelvin(degrees):
    """ This function convert celsius to kelvin."""

    return Decimal(degrees)+ ABSOLUTE_DIFFERENCE


def fahrenheit_to_kelvin(degrees):
    """This function convert fahrenheit to kelvin."""

    # celsius_to_kelvin(fahrenheit_to_celsius())
    celsius = fahrenheit_to_celsius(degrees)
    kelvin = celsius_to_kelvin(celsius)

    return kelvin
