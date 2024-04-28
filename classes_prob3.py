"""
Provides the Room class, which represents a room. The program also 
provides a function, build_grid, which makes a map of rooms.
"""

class Room:
    """
    This class represents a room that can have connections to other rooms.
    The room is initialized with a user selected name.
    Methods: get_name returns the name of the room.
    set_name sets the name of the room.
    collapse_room represents the entrances/exits to the room collapsing, so all
    connections to the room are destroyed from both ends.
    """
    def __init__(self, name):
        self._name=name
        self.n=None
        self.s=None
        self.e=None
        self.w=None
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name=name
    def collapse_room(self):
        adjacent=[self.n, self.s, self.e, self.w]  # all adjacent rooms
        for room in adjacent:
            if room is not None:  # don't need to do anything if no room
                fields=vars(room)  # all rooms adjacent to the adjacent room
                for field in fields:
                    if fields[field] is self:  # close passage leading back
                        fields[field]=None  # from adjacent to collapsed room
        self.n=None
        self.s=None
        self.e=None
        self.w=None

def get_adjacent(grid, i, j):
    """
    This function finds all the adjacent rooms to a given room specified
    by its coordinates in a grid.
    Arguments: grid is a 2D array of Room objects.
    i is an integer.
    j is an integer.
    Return values: adjacent is an array of Room and None objects.
    """
    adjacent=[]
    directions=[(i-1, j), (i+1, j), (i, j+1), (i, j-1)]  # n, s, e, and w
    for direction in directions:
        y=direction[0]
        x=direction[1]
        if y<len(grid) and y>=0 and x<len(grid[i]) and x>=0:  # only appends
            adjacent.append(grid[y][x])  # if a room exists in that direction
        else:                            # (doesn't run off edge of grid)
            adjacent.append(None)
    return adjacent

def room_connections(grid, i, j):
    """
    This function sets the fields of a room specified by its coordinates in
    a grid to the adjacent rooms if those rooms exist.
    Arguments: grid is a 2D array of Room objects.
    i is an integer.
    j is an integer.
    """
    adjacent=get_adjacent(grid, i, j)
    room=grid[i][j]
    room.n=adjacent[0]
    room.s=adjacent[1]
    room.e=adjacent[2]
    room.w=adjacent[3]

def grid_connections(grid):
    """
    This function sets the fields of every room in a grid according to the
    adjacent rooms in the grid.
    Arguments: grid is a 2D array of Room objects.
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            room_connections(grid, i, j)
        
def build_grid(wid, hei):
    """
    This function creates a grid representing a map of Room objects.
    Arguments: wid is an integer.
    hei is an integer.
    Return values: a Room object.
    """
    grid=[]
    for i in range(hei):
        row=[]  # grid is created row by row
        for j in range(wid):
            name=f"{i},{j}"  # ensures each room has a unique name
            row.append(Room(name))
        grid.append(row)
    grid_connections(grid)
    return grid[hei-1][0]  # southwest corner of the grid






