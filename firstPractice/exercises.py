#Assume you're a teacher, write a program to
# 1- read names and total marks of 3 or more students
# 2- rank the top 3 students
# 3- cash reward to 1rst sudent (500), 2nd (300), and 3rd (100)
# 4- statement of appreciation for those with grade from 950
import operator

def studentAwards(studentGrades):
  # print(studentGrades.items())
  # print(sorted(studentGrades))
  sorted_by_grades = sorted(studentGrades.items(), key=operator.itemgetter(1), reverse = True)
  print("The top 3 students are:")
  print("{} with a grade of {}, winning 500$".format(sorted_by_grades[0][0],sorted_by_grades[0][1]))
  print("{} with a grade of {}, winning 300$".format(sorted_by_grades[1][0],sorted_by_grades[1][1]))
  print("{} with a grade of {}, winning 100$".format(sorted_by_grades[2][0],sorted_by_grades[2][1]))

  for k,v in sorted_by_grades:
    if v >= 950:
      print("Good job {}".format(k))
    else:
      print("Keep making progress {}".format(k))


studentGrades = { "Marie": 960, "Ben": 500, "Ella": 955, "Paul": 954, "John":950 }

studentAwards(studentGrades)

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

