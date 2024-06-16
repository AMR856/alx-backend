#!/usr/bin/env python3
"""What can we found in here?"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The indexer can be found in here"""
    the_range_start = 0
    the_range_finish = 0
    while (page > 1):
        the_range_start = the_range_start + page_size
        page = page - 1
    the_range_finish = the_range_start + page_size
    return (the_range_start, the_range_finish)
