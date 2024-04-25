#!/usr/bin/python3
""" finds the peak number """


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    low, high = 0, len(list_of_integers) - 1
    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1
