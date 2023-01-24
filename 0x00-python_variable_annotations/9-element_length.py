#!/usr/bin/env python3
"""Annotate the below function's parameters
   return values with the appropriate types"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element length function"""
    return [(i, len(i)) for i in lst]
