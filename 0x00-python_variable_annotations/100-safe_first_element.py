#!/usr/bin/env python3
"""Adding Annotations to the existing function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Adding Annotations to the existing function"""
    if lst:
        return lst[0]
    else:
        return None
