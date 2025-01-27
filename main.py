# program to find odd numbers in a list

def odd_numbers(lst):
    odd_lst = []
    for i in lst:
        if i % 2 != 0:
            odd_lst.append(i)
    return odd_lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(odd_numbers(lst))