"""
Provides functions to help with solving a 15-peg cracker barrel
puzzle.
https://blog.crackerbarrel.com/2021/08/13/how-to-beat-the-cracker-barrel-peg-game/
"""
def make_board(encoding):
    """
    This function makes a 2D array representing the board from a string 
    specifying which positions have pegs and which are empty.
    Argument: a string (length 15) of 1 and 0 characters.
    Return value: a 2D array of 1 and 0 characters with rows of uneven length.
    """
    board=[]
    start=0
    row_length=1  # first row has one position
    while start+row_length<=len(encoding):  # end of row
        row=[]
        row_positions=encoding[start:start+row_length]  # positions in curr row
        for i in row_positions:
            row.append(i)
        board.append(row)
        start+=row_length  # move to next row
        row_length+=1  # each row has one more position than the last
    return board
        
def print_board(encoding):
    """
    This function prints out a board to the console in an easily understandable
    format, given a string of 1's and 0's representing the board.
    Argument: encoding is a (length 15) string of 1 and 0 characters.
    """
    board=make_board(encoding)
    for i in range(len(board)):
        num_spaces=len(board)-i-1  # spacing to offset row by
        print(" "*num_spaces+" ".join(board[i]))  # print all chars in row

def get_board_index(height, index):
    """
    This function converts the number of a board position (e.g. 1-15) into a
    row and column that can be used to index into the 2D array of the board.
    Argument: height is an integer.
    index is an integer.
    Return value: row is an integer.
    col is an integer.
    """
    temp=index  # used to keep track of how much we still need to move
    row=0
    col=0
    for i in range(height):
        if temp>=i+1:  # if index should be on the next row down
            row+=1
            temp-=i+1  # modify temp to reflect new position
        else:
            col=temp  # remainder - not enough to push to next row
            return row, col

def get_encoding_index(row, col):
    """
    This function converts the row and column of a position in the 2D array
    representing the board to the number of the position (e.g. 1-15)
    Arguments: row is an integer.
    col is an integer.
    Return value: index is an integer.
    """
    index=0
    for i in range(row):
        index+=i+1  # add the length of each row to the total number
    index+=col  # add offset from start of row
    return index

def get_destinations(board, i):
    """
    This function gets half the locations that a specific peg can legally
    move (as well as the peg positions it would hop over), in terms of 2D
    array board indices. Only half are needed because the other half will be
    covered by reversing moves in the caller function.
    Arguments: board is a 2D array representing the shape of the board.
    i is an integer representing the encoding index of the position.
    Return value: a 2D array of tuples of integers.
    """
    height=5  # board has 5 rows
    directions=[]
    row, col=get_board_index(height, i)
    if col+2<len(board[row]):  # if peg can hop to the right
        directions.append([(row, col+1), (row, col+2)])
    if row+2<len(board):  # if peg can hop diagonally down
        directions.append([(row+1, col), (row+2, col)])
        directions.append([(row+1, col+1), (row+2, col+2)])
    return directions
        
def get_all_conceivable_moves():
    """
    This function gets all the legal moves for a 15-peg cracker barrel puzzle
    board as 3 element tuples of the starting position, position that gets 
    hopped over, and end position.
    Return value: an array of tuples of integers.
    """
    board=make_board("0"*15)  # make board using dummy encoding
    moves=set()
    for i in range(15):  # find all moves from each position
        destinations=get_destinations(board, i)
        for destination in destinations:
            over=destination[0]  # ending position
            end=destination[1]  # position that gets hopped over
            over_index=get_encoding_index(over[0], over[1])
            end_index=get_encoding_index(end[0], end[1])
            moves.add((i, over_index, end_index))  # reverse of all legal moves
            moves.add((end_index, over_index, i))  # is also legal
    return moves

def get_moves(encoding):
    """
    This function gets all the legal moves given a specific encoding, or board
    setup. It first generates all the conceivable moves, then selects which
    ones are valid from the current position.
    Argument: encoding is a string of 1 and 0 characters.
    moves is an array of tuples of integers.
    """
    moves=set()
    conceivable_moves=get_all_conceivable_moves()
    for move in conceivable_moves:
        if encoding[move[0]]=="1" and encoding[move[1]]=="1":  # peg hops over
            if encoding[move[2]]=="0":  # peg and lands in empty space
                moves.add(move)
    return moves

def get_new_encoding(move, encoding):
    """
    This function generates a new encoding resulting from a move being made.
    Arguments: move is a tuple of integers.
    encoding is a string of 1 and 0 characters.
    Return value: a string of 1 of 0 characters.
    """
    encoding_list=[i for i in encoding]  # turn into array to be indexed into
    encoding_list[move[0]]="0"
    encoding_list[move[1]]="0"
    encoding_list[move[2]]="1"
    return "".join(encoding_list)  # convert back to string

def cb_all(encoding):
    """
    This function gets all possible solutions given an initial board state and
    returns them as lists of moves to get from the starting condition to a
    solved board.
    Argument: encoding is a string of 1 and 0 characters.
    Return value: solutions is a 2D array of tuples of integers.
    """
    total=0
    for i in encoding:
        total+=int(i)
    if total==1:  # only one position has a peg, meaning board is solved
        return [[]]  # base case; returns 2D array to be built off of
    solutions=[]
    moves=get_moves(encoding)
    for move in moves:
        new_encoding=get_new_encoding(move, encoding)  # hypothetical new state
        histories=cb_all(new_encoding)  # all paths leading to solved state
        for history in histories:
            if history!=None:  # add move to beginning of every valid solution
                solutions.append([move]+history)
    return solutions

def cb_one(encoding):
    """
    This function gets one possible solution given an initial board state and
    returns it as a list of moves to get from the starting condition to a
    solved board.
    Argument: encoding is a string of 1 and 0 characters.
    Return value: an array of tuples of integers.
    """
    solutions=cb_all(encoding)
    if solutions==[]:  # no solutions
        return None
    return solutions[0]
