def stn(esm):
    return esm.capitalize()

esmha = []
for i in range(10):
    esm = input()
    esmha.append(esm)

stn = [stn(esm) for esm in esmha]
output = "\n".join(stn)

print(output)

