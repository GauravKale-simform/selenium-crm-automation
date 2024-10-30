# for i in range(1,6):
#     for j in range(i):
#         print('*',end=' ')
#     print()
from functools import reduce

from Practice.practice import count

# for i in range(1,6):
#     for j in range(5-i):
#         print('',end=' ')
#     for k in range(1,i+1):
#         print(k,end=' ')
#     print()

# dict1 = {'name':'abc','age':'52','salary':'5000'}
# print(dict1['salary'])
# for i,j in dict1.items():
#     print(i,j)

# str1 = 'hello simform'
# str1_split = str1.split()
# first_word = str1_split[0]
# print(first_word)
# rev_first_name = first_word[::-1]
# print(rev_first_name)
# second_word = str1_split[1]
# print(second_word)
# rev_second = second_word[::-1]
# print(rev_second)
# join_word = first_word[1:] + second_word[3:]
# print(join_word)
# rev = join_word[::-1]
# print(rev)

# num = 10
# result = 1
# for i in range(1,num+1):
#     result *= i
# print(result)

# a = 10
# b = [0,1]
# for i in range(2,a+1):
#     b.append(b[-1]+b[-2])
# print(b)

# a_str = 'Level is Imp'
# a = a_str.strip()
# rev_a = a[::-1]
# if a==rev_a:
#     print('strings are palindrome')
# else:
#     print('palindrome not possible')
# print(a_str.replace('is','are'))
# print(a_str.swapcase())
# print(a_str)
# print(a_str.rsplit(' ',1))

# a = int(input('Enter a number:- '))
# if a > 1:
#     for i in range(2,a):
#         if a % i == 0:
#             print(f'{a} is not a prime number')
#             break
#     else:
#         print('It is a prime number')
# else:
#     print('Number is within the range')

# for i in range(1,51):
#     if i % 2 ==0:
#         print(i,end=' ')

# a = 'This is to test weather the strings are matching are not'
# b = ['t','T','r']
# for i in b:
#     count1 = a.count(i)
#     print(i,count1)

# a = 'babajaajahagavagfcaaaaimdjjjnncncmcmc'
# b = ['a','b','j','n','m']
#
# for i in b:
#     count1 = a.count(i)
#     print(f'letter {i} has occured {count1} times')

# sum1 = lambda x,y : x+y
# print(reduce(sum1,(range(1,51))))

# num = [2,4,5,6]
# square = map(lambda x : x ** 2 ,num)
# print(list(square))
# square = []
# for i in num:
#     result = i * i
#     square.append(result)
# print(square)

# num = list(range(1,51))
# even_num = filter(lambda x : x % 2 == 1,num)
# print(list(even_num))

# a = [9,15,63,14]
# sum = reduce(lambda x,y : x+y ,a)
# print((sum))


a = 'he my name is simform'
for




