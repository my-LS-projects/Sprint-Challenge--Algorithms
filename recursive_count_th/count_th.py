"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


# word is a string
# count all occurences of "th" within string, case sensitive
# use recursion
count = 0


def count_th(word):
    count = 0
    if not word:
        return 0
    else:
        if word[:2] == "th":
            count = 1
        else:
            pass
        return count + count_th(word[1:])
    pass
