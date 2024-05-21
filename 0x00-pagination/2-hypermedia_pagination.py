#!/usr/bin/env python3
"""module to create class method to return the appropriate page
of a dataset"""
import csv
import math
from typing import List, Tuple, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page, page_size):
        """returns the start and end indexes of a page"""
        end_index = page * page_size
        start_index = end_index - page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns the appropriate page of a dataset"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        indexes = self.index_range(page, page_size)
        start_index = indexes[0]
        end_index = indexes[1]
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size:
                  int = 10) -> Dict[str, Union[int, List[List], None]]:
        """returns a dictionary containing key-value pairs
        page_size, page, data and next_page"""
        content = self.get_page(page, page_size)
        rows = len(self.dataset())
        total_pages = math.ceil(rows / page_size)
        next_page = page + 1 if page < total_pages else None
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        if total_pages % 1 != 0:
            total_pages += 1
        return {'page_size': page_size, 'page': page, 'data': content,
                'next_page': next_page, 'prev_page': prev_page,
                'total_pages': int(total_pages)}
