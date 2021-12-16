n = int(input("adad ro bego : "))
if n % 2 == 0 and n != 2:
    print('it is not a prime number')
else:
    for i in range (3, (int(n**0.5)+1), 2):
        if n % i == 0:
            print('it is not a prime number')
            break
    else:
        print("it is a prime number")
