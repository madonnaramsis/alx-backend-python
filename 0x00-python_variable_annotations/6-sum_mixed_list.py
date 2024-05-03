#!/usr/bin/env python3
"""Type-annotated sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats"""
    return sum(mxd_lst)
