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


#write a program to print numbers from 1 to 10
for number in range(1,11):
  print(number, end = '')

#write a program to print the sum of odd number from 1 to 10
sumOfOdd = 0

for number in range(1,11)
  if number%2 == 0:
    continue
  else:
    sumOfOdd += number

#Write a program to check if a given number is prime or not

number = 2

for i in range(2, number)
  if number%i = 0:
    print("not prime")
    break
  else:
    print("prime")

