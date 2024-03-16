## Leetcode

# class Solution(object):
#     def twoSum(self, nums, target):
#         sum = {}
#         for i in range(len(nums)):
#             diff = target - nums[i]
#             if diff in sum:
#                 return [sum[diff], i]
#             else:
#                 sum[nums[i]] = i   



# obj = Solution()
# print(obj.twoSum([2,15,7,11], 9))




# Hackerrank

# List Comprehenion
# Question: Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.


# x = 1
# y = 1
# z = 2
# n = 3
# matrix = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]

# print(matrix)


# same question without list comprehension 
# x = 1
# y = 1
# z = 2
# n = 3
# output = []
# abc = []
# for X in range(x+1):
#     for Y in range(y+1):
#         for Z in range(z+1):
#             if X+Y+Z != n:
#                 abc = [X,Y,Z]
#                 output.append(abc)
# print(output)




# arr = [2,3,6,6,5]

# x = arr.remove(max(arr))
# print(arr)
# x = max(arr)
# y = []
# for i in range(len(arr)):
#     if x == arr[i]:
#         y.append(arr[i])
# print()


# s = set(arr)
# print(s)

# x = s.remove(max(s))






# user = 153
# l = len(str(user))
# sum = 0

# while user > 0:
#     digit = user % 10
#     sum = sum + digit**l
#     user = user // 10  

# if sum == user:
#     print("Number is Armstrong...") 
# else:
#     print("Number is Not Armstrong..")   


import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

if __name__ == "__main__":
    # Input the number of test cases
    t = int(input())

    # Input regex patterns and check their validity
    for _ in range(t):
        pattern = input()
        print(is_valid_regex(pattern))