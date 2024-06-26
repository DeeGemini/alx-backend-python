#!/usr/bin/env python3
"""
Script to test the sum_mixed_list function.
"""
sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)

print(sum_mixed_list.__annotations__)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))

