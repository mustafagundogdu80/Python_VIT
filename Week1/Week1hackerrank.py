# Hackerrank 1

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a+b)
#     print(a-b)
#     print(a*b)
"""---------------------------------------------------"""
# Hackerrank 2

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     max_score = second_score = -101
#     for i in arr:
#         if i > max_score :
#             second_score = max_score
#             max_score = i
#         elif i > second_score and i < max_score :
#             second_score = i
#     print(second_score)
"""---------------------------------------------------"""
# Hackerrank 3

# if __name__ == '__main__':
#     n = int(input())
#     str_list = ""
#     for i in range(1,n+1):
#         str_list += str(i)
#     print(str_list)
"""---------------------------------------------------"""
# Hackerrank4

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#     # The variable in which the sum of the notes is kept
#     scores_sum = 0
#
#     for i in student_marks[query_name]:
#         scores_sum += i
#     # Variable whose average values will be printed
#     avarage_str = f"Avarage = {(scores_sum/len(student_marks[query_name])):.2f}"
#     print(avarage_str)
"""---------------------------------------------------"""
# regex_integer_in_range = r"_________"  # Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"_________"  # Do not delete 'r'.
#
# import re
#
# P = input()
#
# print(bool(re.match(regex_integer_in_range, P))
#       and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
#
# number_examined_list = list()
# for i in range(len(regex_alternating_repetitive_digit_pair) - 2):
#     if (regex_alternating_repetitive_digit_pair[i] == regex_alternating_repetitive_digit_pair[i + 2] and
#             regex_alternating_repetitive_digit_pair[i] != regex_alternating_repetitive_digit_pair[i + 1]):
#         number_examined_list.append[regex_alternating_repetitive_digit_pair[i]]
# print(len(number_examined_list) > 0)

"""---------------------------------------------------"""
# import sys
# K = sys.stdin.readline()
# if "\\n" in K :
#     K.replace("\\n","")
#
# room_number_str = sys.stdin.readline()
# if "\\n" in room_number_str:
#     room_number_str.replace("\\n","")
# room_number_list = room_number_str.split(" ")
# captain_room_number = 0
# for i in room_number_list:
#     if room_number_list.count(i) == 1:
#         captain_room_number = i
#         break
# sys.stdout.write(captain_room_number)

"""---------------------------------------------------"""
# import xml.etree.ElementTree as etree
#
# maxdepth = 0
# def depth(elem, level):
#     global maxdepth
#     # your code goes here
#
#     for child in elem:
#         max_depth = max(max_depth, depth(child, level + 1))
#     return max_depth + 1
# if __name__ == '__main__':
#     n = int(input())
#     xml = ""
#     for i in range(n):
#         xml =  xml + input() + "\n"
#     tree = etree.ElementTree(etree.fromstring(xml))
#     depth(tree.getroot(), 0)
#     print(maxdepth)

"""---------------------------------------------------"""
# import xml.etree.ElementTree as etree
#
# maxdepth = 0
# def depth(elem, level):
#     global maxdepth
#     # your code goes here
#     level += 1
#     for child in elem:
#         maxdepth = max(maxdepth,depth(child,level))
#     return level +1
# if __name__ == '__main__':
#     n = int(input())
#     xml = ""
#     for i in range(n):
#         xml =  xml + input() + "\n"
#     tree = etree.ElementTree(etree.fromstring(xml))
#     depth(tree.getroot(), 0)
#     print(maxdepth)


"""---------------------------------------------------"""
# if __name__ == '__main__':
#     N = int(input())
#     consider_list = list()
#     for i in range(N):
#         consider_list.append(input().split())
#     arr = list()
#     for i in consider_list:
#         if i[0] == "insert" :
#             arr.insert(int(i[1]),int(i[2]))
#         elif i[0] == "print" :
#             print(arr)
#         elif i[0] == "remove":
#             arr.remove(int(i[1]))
#         elif i[0] == "append":
#             arr.append(int(i[1]))
#         elif i[0] == "sort":
#             arr.sort()
#         elif i[0] == "pop":
#             arr.pop()
#         elif i[0] == "reverse":
#             arr.reverse()

"""---------------------------------------------------"""
