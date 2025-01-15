# # Week 4 Hackering Questions
# # Q1
# # https://www.hackerrank.com/challenges/diagonal-difference/problem

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'diagonalDifference' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts 2D_INTEGER_ARRAY arr as parameter.
# #

# def diagonalDifference(arr):
#     # Write your code here
#     diagonal1 = 0
#     diagonal2 = 0
#     for i in range(len(arr)):
#         diagonal1 += arr[i][i]
#         diagonal2 += arr[i][len(arr) - 1 - i]
#     return abs(diagonal1 - diagonal2)
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

"""--------------------------------------------------------"""
# # Q2
# # https://www.hackerrank.com/challenges/array-left-rotation/problem

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'rotateLeft' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. INTEGER d
# #  2. INTEGER_ARRAY arr
# #

# def rotateLeft(d, arr):
#     # Write your code here
#     new_arr = []
#     for i in range(len(arr)):
#         new_arr.append(arr[(i+d) % len(arr)])
#     return new_arr
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     d = int(first_multiple_input[1])

#     arr = list(map(int, input().rstrip().split()))

#     result = rotateLeft(d, arr)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

"""--------------------------------------------------------"""
# # Q3
# # https://www.hackerrank.com/challenges/counter-game/problem
# #
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'counterGame' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts LONG_INTEGER n as parameter.
# #

# def counterGame(n):
#     # Write your code here
#     move_counter = 0
#     move_result = n
#     power2= False
#     while move_result != 1:
#         move_counter += 1
#         if not power2:
#             power = 0
#             while 2**power < move_result:
#                 power += 1
#             if 2**power == move_result:
#                 power2 == True
#                 move_result /= 2
#             else:
#                 move_result -= 2**(power-1) 
#         else:
#             move_result /=2
#     return "Louise" if move_counter % 2 == 1 else "Richard"

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         result = counterGame(n)

#         fptr.write(result + '\n')

#     fptr.close()

"""--------------------------------------------------------"""
# # Q4
# # https://www.hackerrank.com/challenges/python-time-delta/problem
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# from datetime import datetime

# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     dt1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
#     dt2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
#     result = int(abs((dt1-dt2).total_seconds()))
#     return str(result)
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         t1 = input()

#         t2 = input()

#         delta = time_delta(t1, t2)

#         fptr.write(delta + '\n')

#     fptr.close()
