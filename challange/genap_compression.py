"""
Buat program yang menerima list bilangan bulat dan mengembalikan list yang hanya berisi bilangan genap, menggunakan list comprehension.
"""

# Diberikan list bilangan, kembalikan list baru berisi hanya bilangan genap dengan urutan yang sama.

def filter_even(nums):
    return [x for x in nums if x % 2 == 0]

print(filter_even([1, 2, 3, 4, 5, 6]))
