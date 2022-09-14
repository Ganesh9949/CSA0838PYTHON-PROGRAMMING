def anagram(s):
    if len(s) % 2 != 0:
        return -1

    dict = {}

    for val in s[len(s)//2:]:
        if val not in dict:
            dict[val] = 0
        dict[val] += 1

    count = 0

    for val in s[:len(s)//2]:
        if val in dict and dict[val] != 0:
            dict[val] -= 1

    for val in dict.values():
        count += val

    return count
