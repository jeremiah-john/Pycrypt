testConstant = 8
newNum = raw_input("pick any number")
newNum = int(newNum)
maximum = 10

newSum = testConstant + newNum
if newSum > maximum: # just precaution
    while newSum > maximum:
        newSum = newSum - maximum;

print newSum
