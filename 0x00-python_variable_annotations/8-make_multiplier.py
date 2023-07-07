#!/usr/bin/env python3

"""
Module: 8-make_multiplier
Description: Contains a function to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    return type is annotated as Callable[[float], float], specifying 
    that the function will return another function that takes a float
    as an argument and returns a float.
    """
    def multiplier_func(number: float) -> float:
        """
        Multiplies a number by the multiplier value.

        Args:
            number (float): The number to multiply.

        Returns:
            float: The multiplied result.
        """
        return number * multiplier

    return multiplier_func
