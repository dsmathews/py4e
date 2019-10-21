# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# fname = input("Enter a file name: ")
# if  len(fname) < 1 : 
#     fname = "mbox-short.txt"
fname = "mbox-short.txt"
fh = open(fname)
lst = list()

counter = 0
for lines in fh :
    if lines.startswith("From:") :
        continue
    elif lines.startswith("From ") :
        counter += 1
        lines.rstrip()
        a = lines.split()
        b = a[1]
        print(b)
print("There were", counter, "lines in the file with From as the first word")