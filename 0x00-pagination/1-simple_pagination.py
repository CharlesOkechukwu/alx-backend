#!/usr/bin/env python3
"""module to create class method to return the appropriate page
of a dataset"""
import csv
import math
from typing import List, Tuple


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
            assert type(page) == int and page > 0
            assert type(page_size) == int and page_size > 0
            indexes = self.index_range(page, page_size)
            start_index = indexes[0]
            end_index = indexes[1]
            return self.dataset()[start_index:end_index]