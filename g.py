#Task2
# n = input('Введите трехзначное число: ')
# m = 0
# if len(n) == 3:
#     for i in n:
#         m += int(i)
#     print(m)
# else:
#     print('Вы ввели не 3-х значное число')

#Task4
# n = int(input('Введите колиство журавликов:'))
# m = n // 4
# k = m*4
# print(f'Петя и Сережа сделали по {m}, шт')
# print(f'Маша сделала , {k} шт')

#Task6
# n = input('Введите 6-значное число: ')
# if len(n) != 6:
#     print(f'Число не 6-ти значное!')
# else:
#     sum1 = 0
#     sum2 = 0
#     for i in range(len(n)//2):
#         sum1 += int(n[i])
#         sum2 += int(n[len(n)//2 + i])
#     if sum1 == sum2:
#         print('Yes!')
#     else:
#         print('No!')

#Task8
n = int(input('1 часть(долька): '))
m = int(input('2 часть(долька): '))
k = int(input('В-те кол-во долек: '))
if k % n == 0 or k % m == 0:
     print('Yes')
else: print('No')
