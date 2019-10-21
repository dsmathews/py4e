# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# file = input("Enter file name")
file = "mbox-short.txt"
fh = open(file)
d = dict()

for lines in fh :
    if lines.startswith("From ") :
        lines.rstrip()
        a = lines.split()
        b = a[1]
        d[b] = d.get(b,0) +1
largest = None
winner = None
for user,count in d.items() :
    if largest is None or count > largest :
        largest = count
        winner = user
print(winner, largest)


