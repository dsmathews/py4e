score = input("Enter Score: ")
s = float(score) * .01
if s >=0.0 and s <=1.0:
    if s >= 0.9:
        print("A")
    elif s >= 0.8:
        print("B")
    elif s >= 0.7:
        print("C")
    elif s >= 0.6:
        print("D")        
    else:
        print("F")
else:
    print("Error. Please use a valid Score between 0-100.")
