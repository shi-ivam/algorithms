from turtle import pos
from torch import max_pool1d


def long(s):
    total_substrings = []
    max = 1
    length = len(s)
    
    for width in range(length,0,-1):
        for position in range(length):
            word = s[position:position+width]
            # print(word)
            
            nonRepeating = True

            l = []
            for i in range(len(word)):
                if (word[i] in l):
                    nonRepeating = False
                else:
                    l.append(word[i])
            if (word not in total_substrings) and nonRepeating:
                total_substrings.append(len(word))
    
    if (not s):
        return 0

    total_substrings.sort()
    return total_substrings[len(total_substrings)-1]
            
    # print(max)
    # print(total_substrings)


    # print(total_substrings)



print(long("qonbyqyqejsmmasmeikjwtrinqukmwdemsikjgdpsxbextqeedpcyimlygxmcbsqtabehetbdwhb"))