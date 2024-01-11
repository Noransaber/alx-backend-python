#!/usr/bin/env python3
def sum_list(input_list: list[float]) -> float:
    """Annotated function
    takes a list of float numbers
    return float sum of them
    """
    sum = 0.0
    for i in input_list:
        sum += i
    return sum
