                     
        
if __name__ == '__main__':
    n = int(input())
    size = n
    letter_list = [chr(i) for i in range(96 +size, 96,-1)]
    print(letter_list)
    # if size > 1 :
    #     for i in range(0,(size * 2)-1):
    #         print_str = ""
    #         if i < size:
    #             for j in range(0, i):
    #                 print_str += letter_list[j]+"-"
    #             print_str += letter_list[i]
    #             if i > 1:
    #                 print_str += print_str[::-1]
                
