# DRY: Don't Repeat Yourself
# number = 1
# dec_number = 1.01
# name = "rishabh"

# data structure: list, dictionary, tuples, sets, tree, graphs
# names = ["ash", "rishab", 89, 1.3, True, False]

# print(names)

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     # steps
#     print(i) # 1      2     3     .....   10
#     print(i+1) # 1 + 1    2+1    3+1....... 11


# for i in range(10): # range(n) -> [0, ..., n-1] [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print("ashish")

# 19

# number = 19

# for i in range(100): # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     #print("19 X " + str(i+1) + "=" + str(number*(i+1))) #BODMAS, type casting, conversion
#     print("19 X ", i+1, "=" , number*(i+1)) # better solution


# 19 X 1 = 19
#  19 X 2 = 38

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(10): # range(10) is -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] this line is expression
#     # the body of loop start here
#     print(i)

# array = ["ash", "rishab", "shaurya", "amit", "ankit"]
# for element in array:
#     # down from here whatever your write will get repeated 5 times
#     print("hello", element)

# print table of 19

# for i in range(10): # range(10) is -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] this line is expression
#     print("19", "X", i+1, "=", 19*(i+1))


# print all the numbers from 1, 1000 that are divisible by 17

# number_to_check = 19
# for i in range(1, 1001): # [1, 2, 3, 4....., 1000] 
#     if i%number_to_check == 0: # == checking if two elements are equal
#         print(i)


# for i in "abdcdklfjaslkdfjlakjfl kjlkajsd flkj flakjsdfl kjasdlfkj ":
#     print(i)

# names =  ["ash", "rishab", "shaurya", "amit", "ankit"]

# for name in names: # here looping over list
#     print(name)
    # for char in name: # "ash"  "rishab" (here looping over string)
    #     print(char)

# names =  ["ash", "rishab", "shaurya", "amit", "ankit"]
# # find and print the length of the names

# for name in names:
#     count = 0
#     for char in name:
#         count = count + 1
#     print(name, count)


# indexing 

# >>> string = "abcdef"
# >>> string
# 'abcdef'
# >>> string[0]
# 'a'
# >>> string[1]
# 'b'
# >>> string[2]
# 'c'
# >>> string[5]
# 'f'
# >>> string[-1]
# 'f'
# >>> names = ["ash", "rishab", "shaurya", "amit", "ankit"]
# >>> names[0]
# 'ash'
# >>> names[1]
# 'rishab'
# >>> names[2]
# 'shaurya'
# >>> names[-1]
# 'ankit'


# print only if name starts with "a"
# names =  ["ash", "rishab", "shaurya", "aurya", "urya", "amit", "ankit"]
# start_char = "a"

# for name in names:
#     if name[0] == start_char: # gets the first char
#         print(name)

# t = (1, 22, 34, 4, 5)
# for i in t:
#     print(i)

# i = 1

# while i <= 10: # if true, run the loop body else exit
#     print(i)
#     i = i + 1

