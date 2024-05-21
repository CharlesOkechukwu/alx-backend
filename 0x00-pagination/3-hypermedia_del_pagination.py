#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """return a dictionary with data and next index even
        if some indexes are deleted"""
        if index is None:
            index = 0
        newlist = []
        all_data = self.indexed_dataset()
        all_keys = sorted(all_data.keys())
        assert index >= 0 and index <= len(all_keys)
        for i in all_keys:
            if i >= index and len(newlist) <= page_size:
                newlist.append(i)
        data = [all_data[d] for d in newlist[:-1]]
        next = newlist[-1] if len(newlist) - page_size == 1 else None
        return {'index': index, 'data': data, 'page_size': len(data),
                'next_index': next}
