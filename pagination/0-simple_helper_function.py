#!/usr/bin/env python3
"""
Simple helper function for pagination
"""

def index_range(page, page_size):
    """
    Returns a tuple of start index and end index
    corresponding to pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)