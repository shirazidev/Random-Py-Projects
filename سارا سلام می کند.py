def hello_check(word):
    right = 'hello'
    right_inx = 0
    
    for hi in word:
        if hi == right[right_inx]:
            right_inx += 1
        if right_inx == len(right):
            return True
        
    return False

inp_word = input()
if hello_check(inp_word) == True:
    print('YES')
else:
    print('NO')