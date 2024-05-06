#!/usr/bin/env python3
"""
This module provides helper functions for managing pagination
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.

    Args:
    page (int): The current page number.
    page_size (int): number of items each page should display

    Returns:
    tuple: containing the start index and the end index
    of the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
