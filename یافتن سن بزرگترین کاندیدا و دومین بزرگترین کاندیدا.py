def find_pirtarin_candida():
    ages = []
    while True:
        age = int(input())
        if age < 0 or age == 1:
            break
        ages.append(age)

    ages.sort(reverse=True)
    print(f"{ages[0]}" , f"{ages[1]}")


find_pirtarin_candida()
