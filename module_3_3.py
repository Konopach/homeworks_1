def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3, 6, False)
print_params('Здарова', 5)
print_params(c = 666)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [33, True, 'Слово']
values_dict = {'a': False, 'b': 11, 'c': 'Ряд'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
