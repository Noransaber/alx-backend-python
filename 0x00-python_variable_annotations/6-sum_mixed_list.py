#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    type-annotated function sum_mixed_list
    which takes a list mxd_lst: integers, floats
    returns: their sum as a float.
    """
    return sum(mxd_lst)
