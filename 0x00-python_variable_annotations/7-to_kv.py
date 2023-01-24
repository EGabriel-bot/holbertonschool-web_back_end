#!/usr/bin/env python3
"""Write a type-annotated function to_kv
   that takes a string and an int OR float as arguments returns a tuple."""

from typing import List, Union, Tuple

types = Union[int, float]


def to_kv(k: str, v: types) -> Tuple[str, float]:
    """ Returs a tuple with the first index being a string
        and the second one being the square of a float"""
    return (k, v * v)
