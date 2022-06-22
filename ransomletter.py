def canMake(ransomNote,magazine):
    k = list(ransomNote)
    l = list(magazine)
    can = True
    for letter in k:
        if (letter in l):
            l.pop(l.index(letter))
        else:
            can = False
            break
    if can:
        return True
    else:
        return False

print(canMake('aa','aab'))