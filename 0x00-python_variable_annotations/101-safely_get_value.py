#!/usr/bin/env python3
"""module for task 11"""
from typing import Any, Mapping, Optional, Sequence, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Optional[T]) -> Union[
        Any, T]:
    """annotating this function"""
    if key in dct:
        return dct[key]
    else:
        return default


annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print(("{}: {}".format(k, v)))
