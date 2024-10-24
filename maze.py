import csv
from colorama import Fore
from random import randrange
def get_maze(): # converts maze txt into array
    lister = []
    temp_row=[]
    txt = open('maze1.txt','r')
    content = txt.readlines()
    txt.close()
    for row in content:
        for item in row:
            temp_row.append(item)
        temp_row.pop(-1)
        lister.append(temp_row)
        temp_row = []
    
    return lister

mazes = get_maze()


def print_maze(maze):
    for row in maze:
        for item in row:
            print(item,end="")

def possible_moves(point_y,point_x, maze):
    possible = []
    if maze[(point_y + -1 )][point_x] == ' ': # one above current point
        possible.append("up")
    if  maze[(point_y + 1 )][point_x] == ' ':
        possible.append("down")
    if maze[point_y][point_x - 1 ] == ' ':
        possible.append("left")
    if maze[point_y][point_x + 1] == ' ':
        possible.append("right")

    return possible

def choose_move(possible):
    amount = len(possible)
    choice = randrange(0,amount)
    final = possible[choice]
    return final


mazes[3][5] = "&"
for row in mazes:
    print(row)



l2 = possible_moves(3,5,mazes)
print(l2)
ce = choose_move(l2)
print(ce)