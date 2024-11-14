# работа со словарем
my_dict = {'Ilya': 1992, 'Anton': 1989, 'Anna': 1996, 'Irina': 1999}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Dmitriy'))
my_dict.update({'Amelia': 2001,
                'Denis': 1994})
print(my_dict.pop('Irina'))
print(my_dict)

# работа с множествами
my_set = {1, 2, 2, 4, 5, 5, "float", 4, "float"}
print(my_set)
my_set.update([6, 8])
my_set.discard(2)
print(my_set)