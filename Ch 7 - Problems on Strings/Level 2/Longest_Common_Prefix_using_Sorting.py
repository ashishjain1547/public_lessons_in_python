"""
Problem Statement: Given a set of strings, find the longest common prefix.
Examples:

    Input: {'wikipediafreeencyclopedia', 'wikipedia', 'wiki', 'wikifree'}
    Output: 'wiki'

    Input: {'apple', 'ape', 'april'}
    Output: 'ap'

    Input: {'apple', 'banana', 'cherry'}
    Output: None

The longest common prefix for an array of strings is the common prefix between 2 most dissimilar strings. For example, in the given array {“apple”, “ape”, “zebra”}, there is no common prefix because the 2 most dissimilar strings of the array “ape” and “zebra” do not share any starting characters. 
"""

in1 = ['wikipediafreeencyclopedia', 'wikipedia', 'wiki', 'wikifree']
in2 = ['apple', 'ape', 'april']
in3 = ['alpha', 'beta', 'gamma']

in_ = in3

in_.sort(key = len)
shortest = in_[0]

c = 0

for i in range(1, len(shortest)):
    s = set()

    for j in in_:
        s.add(shortest[:i] == j[:i])
        if(False in s):
            break
    
    if (len(s) == 1 and True in s):
        c = i

if c > 0:
    print(shortest[:c+1])
