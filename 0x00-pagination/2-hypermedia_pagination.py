#!/usr/bin/env python3
"""Defines Server class."""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size
    in a paginated list.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size

    return (start_index, end_index)


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
        """Retrieves a page of data"""
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieves info about a page"""
        start_idx, end_idx = index_range(page, page_size)
        dataset_len = len(self.dataset())

        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if end_idx < dataset_len else None,
            'prev_page': page - 1 if start_idx > 0 else None,
            'total_pages': math.ceil(dataset_len / page_size)
        }
