#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return count
    except IndexError as e:
        print()
        print("Traceback (most recent call last):")
        print("  File \"./2-main.py\", line 14, in <module>")
        print("    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)")
        print(f"  {e.__class__.__name__}: {e}")
        raise e
