import re
x = "Writing programs (or programming) is a very creative and rewarding activity.  You can write programs for 3036 many reasons, ranging from making your living to solving 7209a difficult data analysis problem to having fun to helping someone else solve a problem.  This book assumes that everyone needs to know how to program, and that once you know how to program you will figure out what you want to do with your newfound skills."
z= "We are surrounded in our daily lives with computers ranging from laptops to cell phones.  We can think of these computers as 4497 our 6702 personal 8454 assistants who can take care of many things 7449 on our behalf.  The hardware in our current-day computers is essentially built to continuously ask us the question, What would you like me to do next?"
y = re.findall('[0-9]+',z)

print(y)