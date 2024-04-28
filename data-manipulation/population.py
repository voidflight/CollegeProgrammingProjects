"""
Reads a user chosen file that
should contains the name of a state or
territory and its population on each line.
The name of the state/territory can come either before or after the population.
The file can contain blank lines and/or comments (lines starting with #).
See the file pop_example_file for an example of formatting.                                            
Displays the state name and population
for each state, as well as the total population
and total number of states.
"""

def separate(line):
    """
    This function separates a
    line in the file into the state name
    and the population of that state.
    Arguments: line is a line in a file.
    Return values: state is a string. pop
    is an integer.
    """
    line_list=line.split()
    for element in line_list:
        if element.isnumeric():
            line_list.remove(element)
            pop=element
            state=" ".join(line_list).strip()
    return state, pop    

def find_state_pops(file):
    """
    This function iterates over every
    line in a file and prints out the state
    name and population on that line. It also
    calculates the total number of states and total
    population.
    Arguments: file is a .txt file
    Return values: num_states is an integer. total_pop
    is an integer.
    """
    total_pop=0
    num_states=0
    for line in file:
        if line.strip()!="":
            if line[0]!="#":
                state, pop=separate(line)
                total_pop+=int(pop)
                num_states+=1
                print("State/Territory:", state)
                print("Population:     ", pop)
    return num_states, total_pop

def main():
    user_input=input("file: ")
    user_input=user_input.strip()
    file=open(user_input, "r")
    num_states, total_pop=find_state_pops(file)
    print("# of States/Territories:", num_states)
    print("Total Population:       ", total_pop)

main()
                    
                    