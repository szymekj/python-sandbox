isPrime = True
a = int (input ("write your number "))
i = 1
while i * i < a:
    i = i + 1
    if a % i == 0:
        isPrime = False
        break

# for b in range (2, a):
#     if a % b == 0:
#         isPrime = False23
#         break
if isPrime:
    print ("it's a prime number")
else:
    print ("sorry it's not a prime number")