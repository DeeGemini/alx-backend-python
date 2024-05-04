#!/usr/bin/env python3
"""
Module to calculate the sum of floats in a list.
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Function to calculate the sum of floats in a list.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of floats in the input list.
    """
    return float(sum(input_list))

