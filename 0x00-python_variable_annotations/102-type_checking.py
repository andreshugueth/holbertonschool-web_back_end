#!/usr/bin/env python3
""" Using mypy """

from typing import List, Union


def zoom_array(lst: List, factor: int = 2) -> List:
    """zoom array

    Args:
        lst (List): List
        factor (int, optional): [description]. Defaults to 2.

    Returns:
        List: new list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
