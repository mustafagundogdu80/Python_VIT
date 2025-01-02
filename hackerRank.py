#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here
    letter_list = [chr(i) for i in range(96 +size, 96,-1)]
    list_print = []
    if size > 1 :
        for i in range(0,size):
            str_print =""
            if i == 0:
                str_print = letter_list[0]
            else:
                for j in range(0,i):
                    str_print += letter_list[j]+"-"
                str_print = str_print+letter_list[i]+str_print[::-1]
            if i != size-1: 
                list_print.insert(0,str_print)
            print(str_print.center(((size-1)*4+1),"-"))
        for i in list_print:
            print(i.center(((size-1)*4+1),"-"))
    elif size == 1:
        print("a")