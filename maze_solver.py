"""
The user is prompted to enter a file name and a command (see main). 
The file should contain a maze, where the open paths in the maze are
represented by #, the start of the maze is represented by S, and the end is
represented by E. Non-open squares should be represented by spaces.
No other characters are allowed.
It's probably better to use a rectangular grid for the maze (i.e. rows and cols
have a fixed length), though I haven't checked whether this is strictly
necessary.

See the file maze_example_file for an example.

The user will see different outputs depending on which command they choose;
the default (if they press enter instead of entering a command) is to display 
a solved version of the maze, where the path is drawn out with dots.
"""
import sys

class TreeNode:
    """
    This class represents a node of a tree. It can have multiple children.
    """
    def __init__(self, val):
        """
        The initializer sets the value of the node and sets the list of
        children to an empty array.
        Argument: val can be any kind of object.
        """
        self.val=val
        self.children=[]
    def add_child(self, val):
        """
        This function makes a child node with a certain value.
        Argument: val can be any kind of object.
        """
        self.children.append(TreeNode(val))

def update_openings(openings, char, j, i):
    """
    This function updates the record of openings to the maze with a
    coordinate specifying the location of the opening, or throws in error if
    the number of openings doesn't match the expected value.
    Arguments: openings is an array of two tuples.
    char is a string, either "S" or "E".
    j is a non-negative integer.
    i is a non-negative integer.
    Return values: openings is an array of two tuples.
    """
    if char=="S":  # start position
        if openings[0]==tuple():  # there isn't already a start position
            openings[0]=(j, i)
        else:
            print("ERROR: The map has more than one START position")
            sys.exit(0)
    elif char=="E":  # end position
        if openings[1]==tuple():  # there isn't already an end position
            openings[1]=(j, i)
        else:
            print("ERROR: The map has more than one END position")
            sys.exit(0)
    return openings
        
def get_coords(file):
    """
    This function retrieves the coordinates for the paths and start and end
    positions in a maze text file.
    Argument: file is a file type object.
    Return values: paths is an array of tuples.
    openings is an array of tuples.
    """
    paths=[]
    openings=[tuple(), tuple()]
    i=0  # keep track of row number
    for line in file:
        line=line.rstrip()  # remove newlines
        for j in range(len(line)):
            if line[j]=="#":  # part of path
                paths.append((j, i))
            elif line[j] in "SE":  # start or end
                openings=update_openings(openings, line[j], j, i)
            elif line[j]!=" ":  # only other valid character is a space
                print("ERROR: Invalid character in the map")
                sys.exit(0)
        i+=1
    if openings[0]==tuple() or openings[1]==tuple():  # no start or end
        print("ERROR: Every map needs exactly one START and exactly one END "\
              "position")
        sys.exit(0)
    return paths, openings

def make_tree(root, cells):
    """
    This function makes a search tree from the coordinate cells of the maze
    that can be used to find a solution.
    Arguments: root is the root node of a tree; in this case it represents the
    start position of the maze.
    cells is a set of tuples of all the coordinates of cells in the maze.
    """
    if cells==set():  # all coordinates have been added to maze
        return
    cells.discard(root.val)  # ensures coordinates are never used twice
    i=root.val[1]  # y and x coords
    j=root.val[0]
    if (j, i-1) in cells:  # go in order of up, down, left, right
        root.add_child((j, i-1))
    if (j, i+1) in cells:
        root.add_child((j, i+1))
    if (j-1, i) in cells:
        root.add_child((j-1, i))
    if (j+1, i) in cells:
        root.add_child((j+1, i))
    for child in root.children:  # recurse into each child
        make_tree(child, cells)

def find_solution(root, end):
    """
    This function finds the solution to a maze using a tree of coordinates to
    search for paths from the start to the end.
    Arguments: root is the root node of a tree and represents the start
    position.
    end is a tuple of integers representing the end position.
    Return value: an array of tuples, representing the coordinates of the path
    from start to end.
    """
    if root.val==end:
        return [end]
    solution=[]
    for child in root.children:
        prev_path=find_solution(child, end)
        if prev_path!=[]:  # will only be non-empty if path leads to end
            solution=[root.val]+prev_path
    return solution

def get_size(cells):
    """
    This function gets the dimensions of a maze.
    Argument: cells is a set of tuples representing the cells of the maze.
    Return values: width is a non-negative integer.
    height is a non-negative integer.
    """
    sorted_cells=sorted(list(cells))  # makes sorted list out of set
    width=sorted_cells[-1][0]+1  # largest width will be at the end
    for i in range(len(sorted_cells)):
        sorted_cells[i]=(sorted_cells[i][1], sorted_cells[i][0])  # swap coords
    sorted_cells=sorted(sorted_cells)
    height=sorted_cells[-1][0]+1  # largest height will now be at the end
    return width, height

def init_grid(width, height):
    """
    This function initializes a grid of a certain size to have all its slots
    filled with spaces.
    Arguments: width is a non-negative integer.
    height is a non-negative integer.
    Return value: grid is a 2D array of strings.
    """
    grid=[]
    for i in range(height):
        row=[]  # make grid row by row
        for j in range(width):
            row.append(" ")
        grid.append(row)
    return grid

def make_map(grid, cells, solution):
    """
    This function fills a grid with map elements, based on information about
    the coordinates of a maze.
    Arguments: grid is a 2D array.
    cells is a set of tuples representing coordinates.
    soltuion is an array of tuples representing coordinates.
    """
    for cell in cells:
        i, j=cell[1], cell[0]
        grid[i][j]="#"  # set all maze cells to paths (#) initially
    for coord in solution:
        i, j=coord[1], coord[0]
        grid[i][j]="."  # overwrite cells in the solution as dots
    start_i, start_j=solution[0][1], solution[0][0]
    end_i, end_j=solution[-1][1], solution[-1][0]
    grid[start_i][start_j]="S"  # overwrite start and end positions
    grid[end_i][end_j]="E"
    
def dump_cells(cells, openings):
    """
    This function displays the coordinates present in the maze to the console.
    Arguments: cells is a set of tuples representing coordinates.
    openings is an array of tuples representing coordinates.
    """
    sorted_cells=sorted(list(cells))
    print("DUMPING OUT ALL CELLS FROM THE MAZE:")
    for cell in sorted_cells:
        disp="  "+str(cell)
        if cell==openings[0]:  # mark the start and end cells
            disp+="    START"
        elif cell==openings[1]:
            disp+="    END"
        print(disp)
    
def print_tree(root, offset="  "):
    """
    This function prints a tree out using a preorder traversal and a spacing
    scheme for visual clarity.
    Arguments: root is the root node of a tree.
    offset is the spacing to print before the node value.
    """
    print(offset+str(root.val))  # start with root
    for child in root.children:  # recurse into each child in order
        print_tree(child, offset+"| ")
        
def dump_tree(root):
    """
    This function displays information about the tree representing the maze
    to the console.
    Argument: root is the root node of a tree.
    """
    print("DUMPING OUT THE TREE THAT REPRESENTS THE MAZE:")
    print_tree(root)

def dump_solution(solution):
    """
    This function displays the coordinates representing the path of the
    solution to the maze to the console.
    Argument: solution is an array of tuples representing coordinates in the 
    maze.
    """
    print("PATH OF THE SOLUTION:")
    for coord in solution:
        print("  "+str(coord))  # includes offset for each coordinate

def dump_size(width, height):
    """
    This function displays information about the size of the maze to the
    console.
    Arguments: width is a non-negative integer.
    height is a non-negative integer.
    """
    print("MAP SIZE:")
    print("  wid:", width)
    print("  hei:", height)

def disp_map(grid):
    """
    This function uses a 2D array of map characters to display a map to the
    console.
    Argument: grid is a 2D array.
    """
    print("SOLUTION:")
    for row in grid:
        print("".join(row))  # prints entire row

def get_input():
    """
    This function gets input from the user and does error checking.
    Return values: command is a string.
    paths is an array of tuples representing coordinates.
    openings is an array of tuples representing coordinates.
    """
    filename=input()
    try:
        file=open(filename, "r")
    except:  # if fille doesn't exist
        print("ERROR: Could not open file: NO_SUCH_FILE")
        sys.exit(0)
    paths, openings=get_coords(file)
    command=input()
    return command, paths, openings

def main():    
    command, paths, openings=get_input()    
    root=TreeNode(openings[0])  # root node represents start of maze
    cells=set(paths+openings)
    make_tree(root, cells.copy())  # make copy so it can be modified
    solution=find_solution(root, openings[1])
    width, height=get_size(cells)
    grid=init_grid(width, height)
    make_map(grid, cells, solution)

    if command=="dumpCells":
        dump_cells(cells, openings)
    elif command=="dumpTree":
        dump_tree(root)
    elif command=="dumpSolution":
        dump_solution(solution)
    elif command=="dumpSize":
        dump_size(width, height)
    elif command=="":
        disp_map(grid)
    else:  # only valid commands are blank line or "dump..."
        print("ERROR: Unrecognized command NOT_A_VALID_COMMAND")

main()