a = int(input("podaj liczbę "))
c = a
b = int(input("podaj 2 liczbę "))
d = b

while True:
    if a == b:
        print("nww to ", a)
        break
    if a > b:
        b = b + d       
    else:
        a = a + c
    