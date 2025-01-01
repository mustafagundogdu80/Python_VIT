# elma = 3
# muz = 3
# if muz > elma:
#     print("Muz Pahalıdır")
# elif elma > muz :
#     print("Elma daha pahalıdır")
# else:
#     print("Fiyatları eşittir")
"""---------------------------------------------------"""
from random import randint

# number = input("Sayı Giriniz: ")
# if (number) == 1 :
    # print("Kazandınız.")
"""---------------------------------------------------"""
# number1 = int(input("Sayı Giriniz: "))
# number2 = int(input("Lütfen ikinci sayıyı giriniz: "))
# if number1>number2 and number1 % number2 == 0 :
#     print("Tam bölünüyor")
# else:
#     print("Tam bölünemiyor.")
"""---------------------------------------------------"""
# number = int(input("Lütfen bir sayı giriniz: "))
# if number == 0:
#     print("Sayı sıfırdır")
# elif number > 0 :
#     print("Sayın pozitiftir.")
# elif number < 0:
#     print("Sayı negatiftir")
"""---------------------------------------------------"""
# number1 = int(input("Lütfen birinci sayıyı giriniz: "))
# number2 = int(input("Lütfen ikinci sayıyı giriniz: "))
# number3 = int(input("Lütfen üçüncü sayıyı giriniz: "))

# if (number1 > number2 and number1 <number3) or (number1 < number2 and number1 > number3):
#     print(number1," ortadır")
# elif (number2 > number1 and number2 <number3) or (number2 < number1 and number2 > number3):
#     print(number2, " ortadır.")
# else:
#     print(f"{number3} ortadır.")
# if ( number2 < number1 <number3) or (number2 >number1 > number3):
#     print(number1," ortadır")
# elif ( number1 < number2 <number3) or (number1 >number2 > number3):
#     print(number2, " ortadır.")
# else:
#     print(f"{number3} ortadır.")

"""---------------------------------------------------"""

# listem = [19, 34, 62, 93]
# number = int(input("Lütfen bir sayı giriniz: "))
#
# for i in listem:
#     if number == i :
#         print(f" {number} sayısı {i} ile eşittir.")
#     elif number > i :
#         print(f" {number} sayısı {i} den büyüktür.")
#     else:
#         print(f" {number} sayısı {i} den küçüktür.")

"""---------------------------------------------------"""
# number = int(input("Sayı giriniz:"))
# for i in range(1,11):
#     print(f"{i}x{number}={number * i}")

"""---------------------------------------------------"""
# in_string =  input("Lütfen bir kelime giriniz: ")
# print("For")
# for i in in_string:
#     print(i)
# print("while")
# counter = 0
# while counter < len(in_string):
#     print(in_string[counter])
#     counter += 1

"""---------------------------------------------------"""
# tahmin_sayi = randint(1,10)
# input_sayi = -1
# test_counter = 0
# while input_sayi != tahmin_sayi :
#     test_counter +=1
#     input_sayi = int(input("Lütfen Sayı giriniz :"))
#     if input_sayi > tahmin_sayi :
#         print("Daha küçük bir sayı giriniz!",end=" ")
#     elif input_sayi < tahmin_sayi :
#         print("Daha büyük bir sayı giriniz!",end="")
# else:
#     print(f"Tebrikler buldunuz! {test_counter} denemenizde buldunuz.")

"""---------------------------------------------------"""

# for i in range(1,101):
#     if i % 3 == 0 and i % 4 ==0 :
#         print(i)

"""---------------------------------------------------"""
# number = int(input("Lütfen sayı giriniz:"))
# for i in range(number,0,-1):
#     if number % i == 0 :
#         print(f"{number} sayısı {i} ile tam bölünebilir.")

"""---------------------------------------------------"""

number1 = int(input("Birinci sayı:"))
number2 = int(input("İkinci sayı:"))
odd_sum = 0
even_sum = 0
add_number = 1
if number1 > number2 :
    add_number = -1
# list_odd= list()
# list_even= list()
for i in range(number1,number2+add_number,add_number):
    if i % 2 == 0:
        # list_even.append(i)
        even_sum += i
    else:
        odd_sum += i
        # list_odd.append(i)
print(f"{number1} ve {number2} arasındaki Tek sayıların toplamı: {odd_sum}, Çift sayıların toplamı: {even_sum}")
# print(sum(list_odd))
# print(sum(list_even))