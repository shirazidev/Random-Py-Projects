def gen_ep(inpexp):
    ones = []
    twos = []
    threes = []

    for soma in inpexp.split('+'):
        if soma == '1':
            ones.append('1')
        elif soma == '2':
            twos.append('2')
        elif soma == '3':
            threes.append('3')
    
    combined = []
    combined.extend(ones)
    combined.extend(twos)
    combined.extend(threes)
    
    exp = '+'.join(combined)
    return exp

vorodi = input()
exp = gen_ep(vorodi)
print(exp)
