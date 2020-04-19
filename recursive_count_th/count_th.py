'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # # An iterative solution to help conceptualize its corresponding recursive solution:
    # count = 0
    # for i in range(0, len(word) - 1):
    #     if word[i] == 't' and word[i + 1] == 'h':
    #         count += 1
    # return count

    def recursive_counter(word, count=0):
        if len(word) <= 1:
            return count
        elif word[0:2] == 'th':
            count += 1
            return recursive_counter(word[2:], count)
        else:
            return recursive_counter(word[1:], count)

    return recursive_counter(word)