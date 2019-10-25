import re
hand = open('regex_sum_307900.txt', "r")
nums = list()
counter = 0
for line in hand :
    # print(line)
    line.rstrip()
    line.split()
    # print(line)
    a = re.findall('[0-9]+', line)
    if len(a) < 1:
        continue
    else:
        # print(a)
        for b in a:
            d = int(b)
            # print(type(b),d)
            nums.append(d)
            counter += 1
c = sum(nums)
avg = int(c/counter)
hand.close()

# print(nums)
print('There are',counter,'items in the NUMS list')
print('The sum of NUMS list is', c) 
# print('The average of NUMS list is', avg)  