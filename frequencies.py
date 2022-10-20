"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        count = 0
        for j in range(len(items)):
            if str(items[i]) == str(items[j]):
                count += 1;
        frequencies.update({str(items[i]):count})
    return frequencies
