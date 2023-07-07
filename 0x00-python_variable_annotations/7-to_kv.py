#!/usr/bin/env python3
'''
Function takes a string and int/float arguments and returns a tuple with the str and square 
of the int/float annotated as a float.
'''

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    '''
    Returns a tuple with a sting and a suare of the integer
    or float "v" annotated as a float
    '''
    return (k, float(v**2))
