# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

# spam = {'name': 'Pooka', 'age': 5}
# spam.setdefault('color', 'black')

def maxNumInList(num):
    return print(max(num))

print('input integer list to find maximum')
userInput = list(input())
maxNumInList(userInput)