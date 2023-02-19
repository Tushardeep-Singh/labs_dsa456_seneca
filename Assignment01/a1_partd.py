# Date of completion : 18th Febuary'2023
# Author : Tushardeep Singh 160427217
from maze import Maze

# Function name : find_path
# Inputs : An instance of Maze (the_maze), start cell ID (from_cell), destination cell ID (to_cell)
# returns [] if no path is possible between from_cell and to_cell, returns from_cell if from_cell = to_cell, else returns path between start and destination using cell ID's (index)
def find_path(the_maze, from_cell, to_cell):
    if(from_cell == to_cell):
        return [from_cell]

    the_maze.mark_cell(from_cell)

    # Function name : mark
    # Inputs : neighbour of from_cell (neighbour)
    # returns True if neighbour is not marked
    # used to shorten if() statements below
    def mark(neighbour):
        if the_maze.get_is_marked(neighbour) == False:
            return True
    
    # Function name : equal_cell
    # Inputs : neighbour of from_cell (neighbour)
    # returns list [from_cell,neighbour], if destination cell (to_cell) is the neighbour
    # used to shorten if() statements below
    def equal_cell(neighbour):
        if(neighbour == to_cell):
            return [from_cell,neighbour]

    # recursion is used below to find a valid path
    to_right = the_maze.get_right(from_cell)
    if(to_right != -1 and mark(to_right)):
        equal_cell(to_right)
        path = find_path(the_maze,to_right,to_cell)
        if path:
            path = [from_cell] + path
            return path
    
    to_left = the_maze.get_left(from_cell)
    if(to_left != -1 and mark(to_left)):
        equal_cell(to_left)
        path = find_path(the_maze,to_left,to_cell)
        if path:
            path = [from_cell] + path
            return path
    
    to_up = the_maze.get_up(from_cell)
    if(to_up != -1 and mark(to_up)):
        equal_cell(to_up)
        path = find_path(the_maze,to_up,to_cell)
        if path:
            path = [from_cell] + path
            return path

    to_down = the_maze.get_down(from_cell)
    if(to_down != -1 and mark(to_down)):
        equal_cell(to_down)
        path = find_path(the_maze,to_down,to_cell)
        if path:
            path = [from_cell] + path
            return path

    # no valid path
    return []
