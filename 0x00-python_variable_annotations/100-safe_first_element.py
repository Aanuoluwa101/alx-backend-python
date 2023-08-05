#!/usr/bin/env python3
"""Augments a given code with the correct duck-typed annotations:
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> \
        Union[typing.Any, None]:
    """Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None