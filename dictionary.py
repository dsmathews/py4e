x = float(input("Enter a number."))

test = {
    "jump":"high",
    "multiply": x * 8,
}
print(type(test))
print(test[1](x))
