#!/usr/bin/env python3
"""
Module to calculate the sum of integers and floats in a mixed list.
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function to calculate the sum of integers and floats in a mixed list.

    Args:
        mxd_lst (List[Union[int, float]]): The mixed list of integers and floats.

    Returns:
        float: The sum of integers and floats in the mixed list.
    """
    return float(sum(mxd_lst))

