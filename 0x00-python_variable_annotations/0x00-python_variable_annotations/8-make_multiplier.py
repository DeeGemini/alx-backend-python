#!/usr/bin/env python3
"""
Module to create a multiplier function.
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function to create a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    def multiplier_func(num: float) -> float:
        """
        Inner function to perform multiplication.

        Args:
            num (float): The input float number.

        Returns:
            float: The result of multiplying num by the multiplier.
        """
        return num * multiplier

    return multiplier_func

