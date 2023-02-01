#!/usr/bin/env python3
""" Task 0 """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ Index_range
        Arguments:
        ---------
            `page`: current page number
            `page_size`: items number in every page
        Return:
        -------
            list for those particular pagination parameters
    """
    start: int
    end: int

    if page == 1:
        start = 0
    else:
        start = (page - 1) * page_size

    end = page * page_size

    return (start, end)
