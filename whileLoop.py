number = input("Enter a number, please: ")
n = float(number)
while n > 0:
    n -= 1
    if n % 15 == 0:
        # print(n)
        print("You've said it all")
    elif n % 5 == 0:
        # print(n)
        print("GO")
    elif n % 3 == 0:
        # print(n)
        print("JACKETS")
    else:
        print (n)
    print("done")

print("Made by George P. Burdell")




