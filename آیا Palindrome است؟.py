def palitrue(a):
    a = a.lower()

    reversed_st = a[::-1]
    return a == reversed_st
a = input()
result = palitrue(a)

if result == True:
    print('palindrome')
else:
    print('not palindrome')