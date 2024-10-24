import csv


def get_maze(): # converts maze txt into array
    lister = []
    temp_row=[]
    txt = open('maze1.txt','r')
    content = txt.readlines()
    txt.close()
    for row in content:
        for item in row:
            temp_row.append(item)
        lister.append(temp_row)
        temp_row = []
            

    return lister

mazes = get_maze()


def print_maze(maze):
    for row in maze:
        for item in row:
            print(item,end="")




print_maze(mazes)