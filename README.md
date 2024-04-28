# CollegeProgrammingProjects

This repository is a compilation of different programming projects I did for class in college. Many of these projects are neither interesting nor useful. However, I no longer have access to a lot of the code I've written over the years (it was saved on a local machine that I no longer own). Other code is built off of other people's repositories, so it it's not a good example of programming I've done by myself.

Most of the code is in Python, but some (which I'll specify below) is in Java.

## puzzle-solvers

The programs in this folder are for solving various puzzles; maze_solver.py is for mazes, word_search.py is for word searches, and cb_solver.py is for 15-peg cracker barrel puzzles. https://blog.crackerbarrel.com/2021/08/13/how-to-beat-the-cracker-barrel-peg-game/

The puzzles need to be given in specific formats, which are described in the python files. I've provided example files for word_search.py and maze_solver.py, which show the proper format. You can run the programs with these example files to see how they're supposed to work.

## recursion

The programs in this folder are just my solutions to various simple recursion practice problems. linked_list_recursion_part2.py implements functions to convert arrays to linked lists, remove every other element of a linked list, and merge two linked lists to a single list (in a particular way - see the file for details). 

annoying_recursion_part2.py implements functions to compute triangle numbers and fibonacci numbers; there's also one that can print out "valleys" of different sizes to the console. It accomplishes these tasks in deliberately weird ways (it was part of the assignment).

## data-manipulation

The programs in this folder do basic file reading and data manipulation. rhymes.py can find rhymes for various words, given a provided pronunciation dictionary. 

population.py and count_items.py are for specific sorts of files - see the program descriptions and example files for more details.

## traveling-salesman

The programs in this folder are written in Java.

They can be used to create and do operations on directed graphs, including solving traveling salesman problems. I've implemented three algorithms: exhaustive search, a heuristic greedy search, and exhaustive search with early stopping.

DGraph.java contains the directed class graph and the implementation of most of these functionalities; PA11Main.java contains some code you can run to put the directed graph into action (e.g. to solve TSPs).

## java-data-structures

The programs in this folder are written in Java.

MyTreeMap.java is a generic implementation of a dictionary using a binary search tree.

PatientQueue.java is a heap implementation of a priority queue.

## misc

classes_prob3.py defines a Room class, which can be used to model a room. It provides code to make maps of rooms/"floorplans".

tree_funcs.py provides some functions for operating on binary trees.

swap.py swaps the front and back halves of a string.


