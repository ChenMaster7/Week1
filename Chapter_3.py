# import time
# import sys
# indent = 0  # How many spaces to indent.
# indentIncreasing = True  # Whether the indentation is increasing or not.
#
# try:
#     while True:  # Main program loop.
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1)  # Pause for 1/10 of a second.
#
#         if indentIncreasing:
#             # Increasing the number of spaces:
#             indent = indent + 1
#             if indent == 20:
#                 # Change direction:
#                 indentIncreasing = False
#
#         else:
#             # Decrease the number of spaces:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()

def collatz(number):
    if number % 2 == 0:
        return number / 2
    if number % 2 == 1:
        return number * 3 + 1


# end of function


print('Please type an integer for the Collatz Sequence')

while True:
    try:
        num = int(input())
        break
    except:
        print('Type an integer number. No decimals')
# end of loop

print(num)
while True:
    if num != 1:
        num = collatz(num)
        print(str(num))
    else:
        print(str(num))
        break
