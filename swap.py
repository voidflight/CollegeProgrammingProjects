"""
The user is prompted to enter a string. 
The front and back halves of the string are then reversed; if there are an
odd number of characters in the string, the middle character remains in place.
Whitespaces are ignored.
The result is then printed to the console.
For instance:
apples -> lesapp
giraffe -> ffeagir
"""

def find_mid(user_input):
    """
    This function finds the middle
    index and corresponding
    character of a string. If the
    string has an even number of
    characters the middle character
    is represented as an empty string.
    Arguments: user_input is a string.
    Return values: mid_i is an integer.
    mid is a string.
    """
    mid_i=int(len(user_input)/2)
    if len(user_input)%2==0:
        mid=""
    else:
        mid=user_input[mid_i]
    return mid_i, mid
    
def main():
    user_input=input("Please give a string to swap: ")
    user_input=user_input.strip()
    mid_i, mid=find_mid(user_input)
    front=user_input[:mid_i]
    back=user_input[-mid_i:]
    print(back+mid+front)

main()
