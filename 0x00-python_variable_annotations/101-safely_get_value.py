#!/usr/bin/env python3
"""Adding Annotations to the existing function"""
from typing import TypeVar, Dict, Any, Optional


K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K,
                     default: Optional[V] = None) -> V:
    if key in dct:
        return dct[key]
    else:
        return default
