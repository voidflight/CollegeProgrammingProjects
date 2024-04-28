"""
The user enters a file name; each line of the file should contain a single word
and then a number, separated by a space.
There can also be blank lines and comments (lines which start with #), which
will be ignored.      
See the file counts_example_file for an example of the proper formatting.                                      
Some lines may contain duplicate words. The "sum" for each word
is computed; for instance, if we have:
    
cherry 5
melon 3
cat 6
cherry 3,

cherry would have the number 8 associated with it,
melon would have the number 3 associated with it,
and cat would have the number 6 associated with it.    

This program computes and displays a few different things:

1. (sum, word) tuples, ordered alphabetically by the words
2. (sum, word) tuples, ordered (ascending) by the sums
3. Each word and sum printed on its own line, ordered (ascending) by the sums

For instance, in the above example we'd see:

(6, "cat"), (8, "cherry"), (3, "melon")

(3, "melon"), (6, "cat"), (8, "cherry")

melon 3
cat 6
cherry 8
"""

def make_dict(file):
    """
    This function converts
    the file into a dictionary.
    Arguments: file is a .txt file opened 
    in read mode.
    Return value: counts is a dictionary 
    mapping strings to integers.
    """
    counts={}
    for line in file:
        if line.strip()!="":
            if line[0]!="#":
                line_list=line.split()
                key=line_list[0]
                value=int(line_list[1])
                if key not in counts:
                    counts[key]=0
                counts[key]+=value
    return counts

def dict_contents(counts):
    """
    This function prints out the contents
    of a dictionary sorted by the keys.
    Arguments: counts is a dictionary mapping keys
    to integers.
    Return value: key_list is a sorted list of strings.
    """
    print("STEP 1: THE ORIGINAL DICTIONARY")
    key_list=list(counts.keys())
    key_list.sort()
    for key in key_list:
        print("  Key:", key, "Value:", counts[key])
    print()
    return key_list

def make_list(counts, key_list):
    """
    This function turns a dictionary into a list
    of tuples where the value comes first in each
    tuple and then sorts the list by value.
    Arguments: counts is a dictionary mapping
    strings to integers. key_list is a sorted list
    of the keys in counts.
    Return value: tuple_list is a sorted list of
    tuples of the values and keys in counts.
    """
    print("STEP 2: A LIST OF VALUE->KEY TUPLES")
    tuple_list=[]
    for key in key_list:
        tuple_list.append((counts[key], key))
    print(tuple_list)
    print()
    print("STEP 3: AFTER SORTING")
    tuple_list.sort()
    print(tuple_list)
    print()
    return tuple_list

def sorted_output(tuple_list):
    """
    This function print the contents of
    a list of tuples to the console.
    Arguments: tuple list is a list of tuples.
    """
    print("STEP 4: THE ACTUAL OUTPUT")
    for i in range(len(tuple_list)):
        print(tuple_list[i][1], tuple_list[i][0])

def main():
    user_input=input("File to scan: ")
    user_input=user_input.strip()
    file=open(user_input, "r") 
    counts=make_dict(file)
    key_list=dict_contents(counts)
    tuple_list=make_list(counts, key_list)
    sorted_output(tuple_list)

main()
    
    
            

