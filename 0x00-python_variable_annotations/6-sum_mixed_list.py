
from typing import Union
def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """
    type-annotated function sum_mixed_list
    which takes a list mxd_lst: integers, floats
    returns: their sum as a float.
    """
    sum = 0.0
    for i in mxd_lst:
        sum += i
    return sum
