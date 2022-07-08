a = int(input('Vvedite chislo'))
count = 0
while a >= 5:
    # а = а-5

    a -= 5
    count += 1
    if a <= 0:
        print("Конец")
    else:
        print(count)
        print(a)



