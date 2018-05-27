#     for x in slst:



def search (s, slst, size):
    for x in range(size):
        if slst[x] == s:
            return x

    return -1




print(search("bog",["ape","cat","dog","bog"],4))

