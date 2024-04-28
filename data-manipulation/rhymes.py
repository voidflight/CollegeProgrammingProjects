"""
The user is prompted to enter a file name. The file should be a pronunciation
dictionary; each line should contain a word followed by its phonemes
(separated by spaces). If a word has multiple pronunciations, there can be
multiple lines for that word. 

The words need to be in all uppercase. The phonemes all need to have a
consistent formatting (e.g. all lower, all upper).

The user can then enter words, one by one, and, for each one, the program
will display all rhymes (according to the pronunciation dictionary) for that
word. This means the words have to be in the dictionary.
"""

def get_file():
    """
    This function gets a file name from the user and opens the file with that
    name in read mode.
    Return value: file is a file object opened in read mode.
    """
    filename=input()
    file=open(filename, "r")
    return file

def make_dictionary(file):
    """
    This function places the contents of a pronunciation dictionary file in a
    dictionary object so that it can be more easily used and accessed by the
    program.
    Argument: file is a file object.
    Return value: dictionary is a dictionary mapping word strings to 2D arrays
    of the phoneme strings representing those words' pronunciations.
    """
    dictionary={}
    for line in file:
        entry=line.strip().split()  # remove newline and split on whitespaces
        word=entry[0]
        phonemes=entry[1:]
        if word not in dictionary:  # create a new entry
            dictionary[word]=[]
        dictionary[word].append(phonemes)  # handles multiple pronunciations
    return dictionary

def get_pronunc(word, dictionary):
    """
    This function finds the pronunciations of a word if it is contained in
    the dictionary.
    Arguments: word is a string.
    dictionary is a dictionary mapping strings to 2D arrays of strings.
    Return value: either a 2D array of strings or a None type object.
    """
    word=word.upper()  # case insensitive search
    if word in dictionary:
        return dictionary[word]
    return None  # if word's pronunciation isn't in dictionary

def split_phonemes(phonemes):
    """
    This function splits the phonemes of a word into the stressed phoneme and
    everything following it, and the phoneme right before the stressed one.
    Argument: phonemes is an array of strings.
    Return values: precede is a string or a None type object.
    end is a string.
    """
    stress=0
    for i in range(len(phonemes)):
        if "1" in phonemes[i]:  # finds stressed phoneme
            stress=i
        if stress!=0:  # if stressed phoneme isn't first
            precede=phonemes[stress-1]
        else:  # is stressed phoneme is first, there is no preceding phoneme
            precede=None
        end=phonemes[stress:]
    return precede, end
            

def is_rhyme(pronunc1, pronunc2):
    """
    This function determines if the pronunciations of two words rhyme with
    each other.
    Arguments: pronunc1 is a 2D array of strings.
    pronunc2 is a 2D array of strings.
    Return value: a Boolean
    """
    for phonemes in pronunc1:  # handle multiple pronunciations
        precede1, end1 = split_phonemes(phonemes)
        for phonemes in pronunc2:
            precede2, end2 = split_phonemes(phonemes)
            if not precede1 or not precede2:  # if stressed phoneme is first
                return False
            if precede2!=precede1 and end2==end1:  # checks for perfect rhymes
                return True
    return False

def get_rhymes(word, dictionary):
    """
    This function finds all the rhymes of a word that are contained in the
    dictionary.
    Arguments: word is a string.
    dictionary is a dictionary mapping strings to 2D arrays of strings.
    Return value: rhymes is an array of strings.
    """
    pronunc1=get_pronunc(word, dictionary)
    rhymes=[]
    if pronunc1 is not None:  # if word's pronunc was found in dictionary
        for entry, pronunc2 in dictionary.items():
            if is_rhyme(pronunc1, pronunc2):
                rhymes.append(entry)
    return rhymes

def show_rhymes(word, dictionary):
    """
    This function prints a message to the console showing the rhymes of a word
    if they exist.
    Arguments: word is a string.
    dictionary is a dictionary mapping strings to 2D arrays of strings.
    """
    rhymes=get_rhymes(word, dictionary)
    rhymes.sort()  # show rhymes in alphabetic order
    print("Rhymes for:", word.upper())
    if len(rhymes)==0:  # word has no rhymes
        print("  -- none found --  ")
    else:
        for rhyme in rhymes:
            print("  "+rhyme)
    
            
def handle_word(word, dictionary):
    """
    This function prints a message to the console that gives the user
    information about their input word.
    Arguments: word is a string.
    dictionary is a dictionary mapping strings to 2D arrays of strings.
    """
    if word.strip()=="":  # blank line
        print("No word given")
    elif len(word.split())!=1:  # multiple words on a line
        print("Multiple words entered, please enter only one word at a time.")
    else:
        show_rhymes(word, dictionary)    
    print()        
    
def main(): 
    file=get_file()
    dictionary=make_dictionary(file)
    while True:
        try:
            word=input()
            handle_word(word, dictionary)
        except Exception:  # end at EOF
            break

main()
        