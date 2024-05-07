#!/usr/bin/env python3
"""
This module provides helper functions for managing pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
    page (int): The current page number.
    page_size (int): number of items each page should display

    Returns:
    Tuple[int, int]: contains the start index and the end index
    of the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
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
        """
        Get a page of the dataset based on the page number
        and page size provided.

        Args:
        page (int): The page number, starting from 1.
        page_size (int): The number of records per page.

        Returns:
        List[List[str]]: A list of data rows from the dataset
        that fall within the page calculated.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index < len(dataset):
            return dataset[start_index:end_index]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page of the dataset along with hypermedia
        information about pagination.

        Args:
            page (int): Page number.
            page_size (int): Number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing page size,
                            page number, data for the page,
                            next & previous page numbers, & total pages
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
