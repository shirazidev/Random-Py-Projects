dot = '.'
def apply(inp):
    vowels = 'aeiou'
    silents = 'bcdfghjklmnpqrstvwxyz'
    moded = ''
    for kochik in  inp:
        if kochik.lower() in vowels:
            continue
        elif kochik.lower() in silents:
            moded += dot + kochik.lower()
        else:
            moded +=kochik

    return moded


    
vorodi = input()
a = apply(vorodi)
print(a)

