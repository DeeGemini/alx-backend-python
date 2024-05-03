#!/usr/bin/env python3
"""
Module to convert a string and int/float to a tuple.
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to create a tuple with string k and the square of int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: The tuple containing k and the square of v as a float.
    """
    return (k, float(v**2))

