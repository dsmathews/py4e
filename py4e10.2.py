# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#Desired Output 
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle :
    if line.startswith("From ") :
        line.rstrip()
        words = line.split()
        for w in words :
            x = w.find(":")
            if x > 0 :
                w.split(":")
                h = w[0:2]
                di[h] = di.get(h,0) + 1
            else:
                continue
comp = list()
for k,v in di.items():
    tups = (k,v)
    comp.append(tups)
comp = sorted(comp)
for k,v in comp:
    print(k,v)