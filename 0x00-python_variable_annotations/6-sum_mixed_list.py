#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list
   takes a list of integers and floats and returns their sum as a float."""

from typing import List, Union

types = Union[int, float]


def sum_mixed_list(mxd_lst: List[types]) -> float:
    """ Returns the sum of a mixed list as a float """
    return sum(mxd_lst)
