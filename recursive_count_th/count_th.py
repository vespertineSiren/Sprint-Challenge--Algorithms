'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    if "th" == word[0:2]:
        count = 1 + count_th(word[1:])
    else:
        return 0
    return count
