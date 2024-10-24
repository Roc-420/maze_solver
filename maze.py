import csv
from colorama import Fore
from random import randrange
from emoji import emojize
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
        print("")


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
        possible.append("right")
        possible.append("right")
   

    return possible

    


def choose_move(possible):
    amount = len(possible)
    choice = randrange(0,amount)
    final = possible[choice]
    return final

# creates a path to the e
# nd of the maze


def find_path(maze,current_y,current_x):
  
    maz = maze
    maz[current_y][current_x] = "&"

    while True:
        
        moves = possible_moves(current_y,current_x,maz)
        if len(moves) == 0:
            return maz, current_y, current_x
    
        else:
            choice = choose_move(moves)
            # appends choice to array
            if choice == "right":
                maz[current_y][current_x + 1] = "&"
                current_x +=1
            elif choice == "left":
                maz[current_y][current_x - 1] = "&"
                current_x -= 1
            elif choice == "up":
                maz[current_y - 1 ][current_x] = "&"
                current_y -= 1
            elif choice == "down":
                maz[current_y + 1 ][current_x] = "&"
                current_y += 1
   
solved = False
def bot_loop():
    while True:
        mazes = get_maze()
        maze, current_y, current_x= find_path(mazes,11,1)
        if maze[(current_y + -1 )][current_x] == 'A': # one above current point
            print("win!!")
            print_maze(maze)
            break

        if  maze[(current_y + 1 )][current_x] == 'A':
            print_maze(maze)
            print("win!!")
            break

        if maze[current_y][current_x - 1 ] == 'A':
            print_maze(maze)
            print("win!!")
            break
            

        if maze[current_y][current_x+1] == 'A':
            print_maze(maze)
            print("win!!")
            break
     
bot_loop()