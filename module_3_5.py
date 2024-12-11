# def get_multiplied_digits(number):
#     str_number = str(number)
#     first = int(str_number[0])
#     if len(str_number) >  1:
#         return  first * get_multiplied_digits(int(str_number[1:]))
#     elif first == 0:
#         return 1
#     return first
#
# result = get_multiplied_digits(40203)
# print(result)
# result2 = get_multiplied_digits(402030)
# print(result2)

def get_multiplied_digits(number):
    str_number = str(number)
    str_number = str_number.replace('0', '')  # попробовал не как на вебинаре записать условие
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)