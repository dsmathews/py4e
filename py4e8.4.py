fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for lines in fh:
    lines.rstrip()
    a = lines.split()
    for word in a:
        if word not in lst:
            lst.append(word)
        else:
            continue
lst.sort()
print(lst)
