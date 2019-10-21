file = "mbox-short.txt"
fh = open(file)
d = dict()
largest = None
winner = None

for lines in fh :
    if lines.startswith("From ") :
        lines.rstrip()
        a = lines.split()
        b = a[1]
        d[b] = d.get(b,0) +1
for user,count in d.items() :
    if largest is None or count > largest :
        largest = count
        winner = user
print(winner, largest)