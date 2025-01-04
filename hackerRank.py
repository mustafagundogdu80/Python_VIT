#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# def print_rangoli(size):
#     # your code goes here
#     letter_list = [chr(i) for i in range(96 +size, 96,-1)]
#     list_print = []
#     if size > 1 :
#         for i in range(0,size):
#             str_print =""
#             if i == 0:
#                 str_print = letter_list[0]
#             else:
#                 for j in range(0,i):
#                     str_print += letter_list[j]+"-"
#                 str_print = str_print+letter_list[i]+str_print[::-1]
#             if i != size-1: 
#                 list_print.insert(0,str_print)
#             print(str_print.center(((size-1)*4+1),"-"))
#         for i in list_print:
#             print(i.center(((size-1)*4+1),"-"))
#     elif size == 1:
#         print("a")

"""---------------------------------------------------"""
# # https://www.hackerrank.com/challenges/swap-case/problem
# def swap_case(s):        
#     return s.

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

"""---------------------------------------------------"""
# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from itertools import product

k, m = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(k)]

max_mod_sum = max(sum(x**2 for x in combination) % m for combination in product(*lists))

print(max_mod_sum)  


"""---------------------------------------------------"""