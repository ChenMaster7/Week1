# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]  # list concatenation
# print('The cat names are:')
# for name in catNames:
#     print(' ' + name)

# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
#     print('I do not have a pet named ' + name)
# else:
#     print(name + ' is my pet.')

# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
#     print('Index ' + str(index) + ' in supplies is: ' + item)

# # Conway's Game of Life
# import random, time, copy
# WIDTH = 60
# HEIGHT = 20
#
# # Create a list of list for the cells:
# nextCells = []
# for x in range(WIDTH):
#     column = [] # Create a new column.
#     for y in range(HEIGHT):
#         if random.randint(0, 1) == 0:
#             column.append('#') # Add a living cell.
#         else:
#             column.append(' ') # Add a dead cell.
#     nextCells.append(column) # nextCells is a list of column lists.
#
# while True: # Main program loop.
#     print('\n\n\n\n\n') # Separate each step with newlines.
#     currentCells = copy.deepcopy(nextCells)
#
#     # Print currentCells on the screen:
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(currentCells[x][y], end='') # Print the # or space.
#         print() # Print a newline at the end of the row.
#
#     # Calculate the next step's cells based on current step's cells:
#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             # Get neighboring coordinates:
#             # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
#             leftCoord = (x - 1) % WIDTH
#             rightCoord = (x + 1) % WIDTH
#             aboveCoord = (y - 1) % HEIGHT
#             belowCoord = (y + 1) % HEIGHT
#
#             # Count number of living neighbors:
#             numNeighbors = 0
#             if currentCells[leftCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-left neighbor is alive.
#             if currentCells[x][aboveCoord] == '#':
#                 numNeighbors += 1 # Top neighbor is alive.
#             if currentCells[rightCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-right neighbor is alive.
#             if currentCells[leftCoord][y] == '#':
#                 numNeighbors += 1 # Left neighbor is alive.
#             if currentCells[rightCoord][y] == '#':
#                 numNeighbors += 1 # Right neighbor is alive.
#             if currentCells[leftCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-left neighbor is alive.
#             if currentCells[x][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom neighbor is alive.
#             if currentCells[rightCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-right neighbor is alive.
#
#             # Set cell based on Conway's Game of Life rules:
#             if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
#                 # Living cells with 2 or 3 neighbors stay alive:
#                 nextCells[x][y] = '#'
#             elif currentCells[x][y] == ' ' and numNeighbors == 3:
#                 # Dead cells with 3 neighbors become alive:
#                 nextCells[x][y] = '#'
#             else:
#                 # Everything else dies or stays dead:
#                 nextCells[x][y] = ' '
#     time.sleep(1) # Add a 1-second pause to reduce flickering.

# # Comma Code project
# def commaCode(userList):
#     for n in range(len(userList)):
#         if n != (len(userList) - 1):
#             print(userList[n] + ', ', end='')
#         else:
#             print('and ' + userList[n] + '.')
#
# spam = []
# commaCode(spam)

# """Coin Flip Streaks"""
# import random
# print('Flip coin how many times?')
# numTrials = int(input())
# print('Calculate probability of how many streaks in a row?')
# numStreak = int(input())
# current = []
# numberOfStreaks = 0
# headsStreak = ['H'] * numStreak
# tailsStreak = ['T'] * numStreak
#
# # coin flip generation
# for n in range(numTrials):
#     if random.randint(0,1) == 0:
#         current.append('H')
#     else:
#         current.append('T')
#
#     if n >= numStreak and (current[n-(numStreak-1):n+1] == headsStreak or current[n-(numStreak-1):n+1] == tailsStreak):
#         numberOfStreaks += 1
#
# print('Chance of streak: %s%%' % (numberOfStreaks / numTrials))

"""Character Picture Grid"""
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

numRows = len(grid)
numCol = len(grid[0])
for x in range(0, numRows):
    for y in range(0, numCol):
        print(grid[x][y], end='')
    print()