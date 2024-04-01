#!/usr/bin/env python3
"""
module: 0-simple_helper_function
"""


def index_range(page, page_size):
    """
    Args:
        page: Page number
        page_size: size of the page
    Return:
        Tuple of size two containing start and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
