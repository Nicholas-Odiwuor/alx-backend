#!/usr/bin/env python3
"""
2-hypermedia_pagination.py
Hypermedia pagination implementation.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index for pagination.

    Args:
        page (int): current page number (1-indexed)
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names with hypermedia support."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset based on page and page_size parameters.

        Args:
            page (int): page number, must be a positive integer
            page_size (int): number of items per page, must be a positive integer

        Returns:
            List[List]: list of rows for the requested page or empty list if out of range
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary with pagination information and dataset page.

        Args:
            page (int): page number, must be a positive integer
            page_size (int): number of items per page, must be a positive integer

        Returns:
            Dict[str, Any]: pagination metadata and page data
        """
        data_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        hyper: Dict[str, Any] = {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return hyper

