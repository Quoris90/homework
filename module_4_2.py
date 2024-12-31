def print_params(a=1, b='строка', c=True):  # *args, **kwargs
    print(a, b, c)


values_list = [3, "Fake", 2.1]
values_dict = {'a': 10, 'b': 3.14, 'c': False}
values_list_2 = [[1, 2], [5, 2]]

print_params(c = [1, 2, 3])

print_params(b = 25)
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)




