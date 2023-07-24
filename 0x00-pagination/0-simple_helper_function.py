#!/usr/bin/env python3
"""
Takes a page and page size and
returns the start a nd end index of
data to be returned
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing start and end index """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
