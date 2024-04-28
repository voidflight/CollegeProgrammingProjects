"""
Provides three function that implement recursion in an "annoying" way.
"""

def annoying_triangleNumbers(n):
    """
    This function computes the nth Triangle Number, defined to be the sum of
    numbers from 1 to n.
    Argument: n is a non-negative integer.
    Return value: a non-negative integer.
    """
    if n==0:  # hard-coded up to n=3
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 3
    elif n==3:
        return 6
    elif n==4:  # hard-coded but recursive up to n=6
        return 4+annoying_triangleNumbers(3)
    elif n==5:
        return 5+annoying_triangleNumbers(4)
    elif n==6:
        return 6+annoying_triangleNumbers(5)
    else:  # general recursive case
        return n+annoying_triangleNumbers(n-1)

def annoying_fibonacci_sequence(n):
    """
    This function returns the first n values of the Fibonacci Sequence as an
    array.
    Argument: n is a non-negative integer.
    Return value: an array of integers.
    """
    if n==0:  # hard-coded up to n=3
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]
    elif n==3:
        return [0, 1, 1]
    elif n==4:  # hard-coded but recursive up to n=6
        prev=annoying_fibonacci_sequence(3)  # prev[-2]+prev[-1] is the next
        return prev+[prev[-2]+prev[-1]]  # term in the sequence
    elif n==5:
        prev=annoying_fibonacci_sequence(4)
        return prev+[prev[-2]+prev[-1]]
    elif n==6:
        prev=annoying_fibonacci_sequence(5)
        return prev+[prev[-2]+prev[-1]]
    else:  # general recursive case
        prev=annoying_fibonacci_sequence(n-1)
        return prev+[prev[-2]+prev[-1]]

def annoying_valley(n):
    """
    This function prints an ascii art valley (with a size determined by n)
    to the console.
    Argument: n is a non-negative integer.
    """
    if n==0:  # hard-coded up to n=3
        return
    elif n==1:
        print("*")
    elif n==2:
        print("./")
        print("*")
        print(".\\")
    elif n==3:
        print("../")
        print("./")
        print("*")
        print(".\\")
        print("..\\")
    elif n==4:  # hard-coded but recursive up to n=6
        print("."*3+"/")
        annoying_valley(3)
        print("."*3+"\\")
    elif n==5:
        print("."*4+"/")
        annoying_valley(4)
        print("."*4+"\\")
    elif n==6:
        print("."*5+"/")
        annoying_valley(5)
        print("."*5+"\\")
    else:  # general recursive case
        print("."*(n-1)+"/")
        annoying_valley(n-1)
        print("."*(n-1)+"\\")
