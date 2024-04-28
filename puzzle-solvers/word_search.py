"""
The user is prompted to enter a file name.
The file should contain a word search grid and a list of words to search for,
formatted as follows:
    
The grid should come first. Each row should be a separate line, and should be
represented as a string of characters (no spaces). I.e. each column is a 
character.

There should then be a line break, after which comes the list of words.
Each word should be on its own line.

See word_searcH_example_file for an example.

The locations of each word will be displayed to the console as the word
searcher finds them. Words can be horizontal, vertical, or diagonal; they can
be spelled forwards or backwards.
"""

import sys

def get_file():
    """
    This function prompts the user for a file name.
    It opens the file in read mode if possible,
    and ends the program with an error message
    if not.
    Return value: file is a file object.
    """
    print("Please give the puzzle filename:")
    file_name=input()
    try:
        file=open(file_name, "r")
        return file
    except Exception:
        print("Sorry, the file doesn't exist or cannot be opened.")
        sys.exit(0)  # exits

def make_data(file):
    """
    This function turns the data in a preformated
    file into a 2D array of letters and an array of
    words to be found in the array.
    Arguments: file is a file object.
    Return values: grid is a 2D array of one
    character strings. words is an array of strings
    of any length.
    """
    grid=[]
    words=[]
    for line in file:
        row=[]
        line=line.strip()  # removes newline from end of line in file
        if line=="":  # stops adding to grid when a blank line is found
            break
        else:
            for letter in line:
                row.append(letter)  # make grid row by row
        grid.append(row)
    for line in file:  # starts where the last for loop left off
        line=line.strip()
        words.append(line)  # adds words to be found to an array
    return grid, words

def find_match(grid, word):
    """
    This function determines whether a word
    is contained within a 2D array of letters
    and, if it is, what the indices of the
    letters of the word are.
    Arguments: grid is a 2D array of one character strings.
    words is an array of strings of any length.
    Return values: indices is an array that may be empty
    or contain tuples of integers.
    """
    match=""
    indices=[]
    for i in range(len(grid)):  # iterate through every letter in the grid
        for j in range(len(grid[i])):
            for y_incr in range(-1, 2):  # iterate through all eight directions
                for x_incr in range(-1, 2):
                    y=i  # create temporary index variables so they can be
                    x=j  # modified in the loop
                    while match[:len(match)]==word[:len(match)]:
                        """
                        The algorithm keeps looking in a given direction
                        as long as the combination of letters it's found
                        matches the word of interest so far.
                        """
                        if y>=0 and y<len(grid):  # make sure the search
                            if x>=0 and x<len(grid[0]):  # won't go off grid
                                match+=grid[y][x]
                                indices.append((y, x))
                                y+=y_incr  # take a step in the selected
                                x+=x_incr  # direction (N, SW, etc.)
                                if match==word:  # returns the location of
                                    return indices  # the found word
                            else:  # stops if search hits left or right edge
                                break  # of grid
                        else:  # stops if search hits top or bottom edge of
                            break  # grid
                    match=""  # reset if search from an index in a direction
                    indices=[]  # didn't find the word
    return indices  # return empty list if word not found

def show_match(grid, indices):
    """
    This function displays a version of the grid
    argument where only the letters with the indices
    in the indices argument have the original values.
    Everything else in the grid is a dot. This lets
    the user see where the word they wanted to find
    is located in the grid.
    Arguments: grid is a 2D array of one character
    strings. indices is an array of tuples of integers.
    """
    for i in range(len(grid)): 
        row=""  # make the display one row at a time
        for j in range(len(grid[i])):
            if (i, j) in indices:  # display the grid letter
                row+=grid[i][j]    # if the grid index is an index
            else:                  # of the word of interest, and
                row+="."           # display a dot otherwise
        print(row)

def main():
    file=get_file()
    grid, words=make_data(file)
    for word in words:
        indices = find_match(grid, word)
        if indices==[]:  # indices will be empty if the word wasn't found
            print("Word '" + word + "' not found")
        else:
            show_match(grid, indices)
        print()

main()