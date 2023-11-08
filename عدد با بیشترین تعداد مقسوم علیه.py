javab = 0
talashe_1= 0
tedad = 0

for i in range(1,21):
 adad = int(input())

 for x in range(1, adad+1):
         if adad % x == 0:
            talashe_1+=1
         else:
            x = x + 1

 if talashe_1 > tedad:
     tedad = talashe_1
     javab = adad

 elif talashe_1 == tedad:
    if(adad > javab):
        javab = adad
        tedad = talashe_1

 talashe_1 = 0

print(javab, tedad)