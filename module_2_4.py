numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    if num == 1:
        continue
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print('Primes:', primes)
print('Not primes:', not_primes)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# for elem in numbers:
#     Flag = True
#     for divizor in range(2, elem):
#         if elem % divizor == 0:
#             Flag = False
#             not_primes.append(elem)
#             break
#     if Flag == True and elem != 1:
#         primes.append(elem)
#
# print('Primes:', primes)
# print('Not primes:', not_primes)







