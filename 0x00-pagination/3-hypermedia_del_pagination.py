#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with no cached datasets."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient hypermedia pagination dictionary.

        Args:
            index (int): the start index of the page
            page_size (int): the number of items per page

        Returns:
            Dict: contains 'index', 'next_index', 'page_size', and 'data'
        """
        # Validate arguments
        assert isinstance(index, int) and 0 <= index < len(self.dataset()), "index out of range"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        indexed_data = self.indexed_dataset()
        # Remaining valid indices after deletions
        valid_indices = [i for i in sorted(indexed_data.keys()) if i >= index]

        # Slice out the page
        page_indices = valid_indices[:page_size]
        data = [indexed_data[i] for i in page_indices]

        # Determine next_index
        if len(valid_indices) > page_size:
            next_index = valid_indices[page_size]
        else:
            next_index = None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }

