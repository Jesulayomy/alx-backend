#!/usr/bin/env python3
""" This module indexes pages """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing a start and end index """

    front = (page - 1) * page_size
    back = page_size + front
    return (front, back)
