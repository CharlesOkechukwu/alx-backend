#!/usr/bin/env python3
"""module to create helper function for a page index range"""


def index_range(page, page_size):
    """returns the start and end indexes of a page"""
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
