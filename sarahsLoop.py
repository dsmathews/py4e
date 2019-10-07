number = input("Enter a number, please: ")
n = int(number)
while n > 0:
    n -= 1
    if n % 15 == 0:
        # print(n)
        print("You've said it all")
    elif n % 5 == 0:
        # print(n)
        print("Sarah is sweet")
    elif n % 3 == 0:
        # print(n)
        print("Sarah is silly")
    else:
        print (n)
    print("done")

print("Made by George P. Burdell")
