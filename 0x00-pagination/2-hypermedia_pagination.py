#!/usr/bin/env python3
"""What can we found in here?"""
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Page getter"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        self.dataset()
        if start > len(self.__dataset):
            return []
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """hyper getter"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        next_page = 0
        prev_page = 0
        start, end = index_range(page, page_size)
        data = self.get_page(page, page)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        if page + 1 <= total_pages:
            next_page = page + 1
        else:
            next_page = None
        if page != 1:
            prev_page = page - 1
        else:
            prev_page = None
        my_dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return my_dict
