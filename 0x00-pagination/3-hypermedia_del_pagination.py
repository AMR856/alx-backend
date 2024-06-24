#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
from typing import Dict
import csv
import math
from typing import List


class Section:
    """What is that?"""
    def __new__(cls, start, length):
        return slice(start, start+length)


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
        """Hyper index getter"""
        assert type(index) == int and index <= len(self.__indexed_dataset)
        index_database = self.indexed_dataset()
        data = []
        data_count = 0
        next_index = 0
        start = index if index else 0
        for i, item in index_database.items():
            if i >= start and data_count < page_size:
                data_count = data_count + 1
                data.append(item)
                continue
            if data_count == page_size:
                next_index = i
                break
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
