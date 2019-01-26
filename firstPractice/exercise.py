#Function that checks among the 2 numbers given which one is the max
def findMax(firstNb, secondNb):
  if firstNb > secondNb:
    print("1rst greater")
    return firstNb
  elif secondNb > firstNb:
    print("2nd greater")
    return secondNb
  else:
    print("numbers are equal")
    return firstNb

print("first number?")
firstNb = int(input())
print("second number?")
secondNb = int(input())

maxNb = findMax(firstNb, secondNb)
print("the Max number is: {}".format(maxNb))
