text = "X-DSPAM-Confidence:    0.8475";
opos = None
num_pos = None
for char in text:
    opos = text.find("0")
# print(opos)
for char in text:
    num_pos = text.find("5")
# print(num_pos)
num = text[opos - 1 : num_pos + 1]
new_num = float(num)
print(new_num)

    