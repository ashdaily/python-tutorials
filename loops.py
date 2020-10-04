# DRY: Don't Repeat Yourself
number = 1
dec_number = 1.01
name = "rishabh"

# data structure: list, dictionary, tuples, sets, tree, graphs
names = ["ash", "rishab", 89, 1.3, True, False]

# print(names)

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     # steps
#     print(i) # 1      2     3     .....   10
#     print(i+1) # 1 + 1    2+1    3+1....... 11


# for i in range(10): # range(n) -> [0, ..., n-1] [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print("ashish")

# 19

number = 19

for i in range(100): # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #print("19 X " + str(i+1) + "=" + str(number*(i+1))) #BODMAS, type casting, conversion
    print("19 X ", i+1, "=" , number*(i+1)) # better solution


# 19 X 1 = 19
#  19 X 2 = 38