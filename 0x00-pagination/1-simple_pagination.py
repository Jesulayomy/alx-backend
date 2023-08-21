#!/usr/bin/env python3
""" This module indexes pages with a class """
import csv
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
        """ gets a  page for the dataset """

        assert type(page) == int and page > 0
        assert type(page_size) == int and page > 0

        indexes = index_range(page, page_size)
        self.dataset()
        return self.__dataset[indexes[0]:indexes[1]]
