sen = int(input())
if sen > 0 and sen < 6:
    print('khordsal')
elif sen >= 6 and sen < 10:
    print('koodak')
elif sen >= 10 and sen < 14:
    print('nojavan')
elif sen >= 14 and sen < 24:
    print('javan')
elif sen >= 24 and sen < 40:
    print('bozorgsal')
elif sen >= 40:
    print('miansal')