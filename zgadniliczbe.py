import random
b = 0
liczba = random.randint(1, 100)

while (True):
    a = int(input('zgadnij liczbe którą wymyśliłem: '))
    b = b + 1
    if a == liczba:
        print ("\n\n\n\t\t\tdobrze!!! zgadłeś za " + str(b) +  " razem \n\n\n\n\n")
        break
    elif a > liczba:
        print("\nnie, liczba jest mniejsza\n")
    else:
        print("\nnie, liczba jest większa\n")
