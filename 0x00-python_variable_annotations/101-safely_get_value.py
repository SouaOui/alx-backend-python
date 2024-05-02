#!/usr/bin/env python3
"""Adding Annotations to the existing function"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
V = Union[Any, T]
Res = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: V = None) -> Res:
    """Adding annotations to the existing function"""
    if key in dct:
        return dct[key]
    else:
        return default
