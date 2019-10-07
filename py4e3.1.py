hrs = input("Enter Hours:")
pay = input("Rate of pay:")
h = float(hrs)
p = float(pay)
salary = h * p

if h > 40:
    ot = (h - 40) * (p / 2)
    combined = (salary + ot)
    print("overtime")
    print("Pay: " + str(combined))

else: 
    print("regular time")
    print("Pay: " + str(salary))