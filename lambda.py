from functools import reduce
# number_list = [10,20,30,40,50,66]
# avarage = (lambda x: x + num  for num in number_list)/len(number_list)
# print(avarage)

"""----------------------------------------"""
# list_a = [1,2,3,4,5,6,7,8,9,10]
# print(list_a)
# odd_list = list(filter(lambda x : x % 2 == 1, list_a))
# print(odd_list)

"""----------------------------------------"""
# list_a = [1,2,3,4,5,-5,-4,-3]
# # print(list_a)
# negative_list = list(filter(lambda x : x < 0, list_a))
# print(negative_list)

"""----------------------------------------"""
# numbers=[9, 16, 25, 36, 144]
# square_root = list(map(lambda x: x ** 0.5, numbers))
# print(square_root)

"""----------------------------------------"""
# # def look_nummer(number):
# #     if number % 2 == 0:
# #         return "Even"
# #     else:
# #         return "Odd"
#
# numbers=[1, 2, 3, 4, 5]
# # odd_or_even = list(map(lambda x: look_nummer(x)  , numbers))
# odd_or_even = list(map(lambda x: "Even" if x % 2 == 0 else "Odd"  , numbers))
# print(odd_or_even)

"""----------------------------------------"""
# unsorted_list=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#
# sorted_list = sorted(unsorted_list, key =lambda x: x[1], reverse=True)
#
# print(sorted_list)
