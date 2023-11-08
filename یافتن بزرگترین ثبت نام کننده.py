def pirtarin_candida():
    max_sen = 0

    while True:
        age = int(input())

        if age < 0 or age == 1:
            break

        if age > max_sen:
            max_sen = age

    print(f"{max_sen}")


pirtarin_candida()