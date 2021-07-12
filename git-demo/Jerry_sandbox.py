"""Show odd number from 0 to 100"""
# def oddNum():
#     output = []
#     for num in range(0, 100):
#         if num % 2 == 1:
#             output.append(num)
#     print(output)

# oddNum()


"""Find maximum number from entered list"""
# def maxNumInList(num):
#     num.sort(reverse=True)
#     return print(num[0])

# numInput = []
# print('input integers one by one to create a list. Enter blank to find the maximum from list.')
# while True:
#     userInput = input()
#     if userInput == '':
#         break
#     else:
#         numInput.append(int(userInput))

# maxNumInList(numInput)


"""Leap year calculator"""
# def isLeapYear(inputYear):
#     if ((inputYear % 4 == 0) and (inputYear % 100 != 0)) or (inputYear % 400 ==0):
#         return True
#     else:
#         return False

# userInput = int(input())
# print(isLeapYear(userInput))


"""Check if list is in consecutive number"""
# def isConsecutive(inputList):
#     firstNum = inputList[0]
#     for x in range(len(inputList)):  # for-loop checks if any number is NOT consecutive. Return false if not.
#         if (firstNum + x) != inputList[x]:
#             return False
#     return True  # return true if the for-loop passes

# userInput = []
# while True:
#     x = input('type in an integer. Enter blank to check if list is consecutive.\n')
#     if x == '':
#         break
#     else:
#         userInput.append(int(x))

# print(isConsecutive(userInput))