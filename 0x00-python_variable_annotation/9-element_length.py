#!/usr/bin/env python3
"""
Module to demonstrate duck typing for an iterable object.
"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to calculate the length of elements in an iterable object.

    Args:
        lst (Iterable[Sequence]): The input iterable object.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing elements and their lengths.
    """
    return [(i, len(i)) for i in lst]

