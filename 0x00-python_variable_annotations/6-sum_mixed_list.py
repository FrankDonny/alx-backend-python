#!/usr/bin/env python3
"""sum_mixed_list annotated module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function containing mixed data type list"""
    return sum(mxd_lst)
