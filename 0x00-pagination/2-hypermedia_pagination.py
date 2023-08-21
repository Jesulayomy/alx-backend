#!/usr/bin/env python3
""" This module indexes pages with a class """
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing a start and end index """

    front = (page - 1) * page_size
    back = page_size + front
    return (front, back)


class Server:
    """
        Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
            Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        start, stop = index_range(page, page_size)
        if not self.__dataset:
            self.dataset()
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        try:
            result = [self.__dataset[i] for i in range(start, stop)]
        except (IndexError):
            result = []

        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns a dictionary of implementation of data """

        pages = self.get_page(page, page_size)
        next_page = page + 1
        prev_page = page - 1
        total_pages = math.ceil(len(self.__dataset) / page_size)
        if prev_page == 0:
            prev_page = None
        if next_page > total_pages:
            next_page = None

        result = {
            'page_size': page_size,
            'page': page,
            'data': pages,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return result
