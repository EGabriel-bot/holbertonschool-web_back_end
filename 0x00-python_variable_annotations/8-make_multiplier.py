#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier
   takes a float multiplier as argument
   returns a function that multiplies a float by multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """
    def function(number: float):
        return (number * multiplier)
    return function
