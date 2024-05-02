#!/usr/bin/env python3
"""Annotations in a existing function"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Adding Annotations to the existing function"""
    return [(i, len(i)) for i in lst]
