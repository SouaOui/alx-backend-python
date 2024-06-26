#!/usr/bin/env python3
"""Making changes after checking with mypy"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Making changes after checking with mypy"""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)  # Convert the list to a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Pass an integer as the factor
