import random
b = 0
liczba = random.randint(1, 100)

while (True):
    a = int(input('guess the number from 1 to 100 that I\'m thinking of: '))
    b = b + 1
    if a == liczba:
        print ("\n\n\t\t\tgood!!!! you guessed it after " + str(b) +  " tries \n\n")
        break
    elif a > liczba:
        print("\nno, the number is lower\n")
    else:
        print("\nno, the number is higher\n")
