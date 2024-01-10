#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    net_weight = sum(x[0] * x[1] for x in my_list)
    weight = sum(x[1] for x in my_list)
    return net_weight / weight
