# Use a for loop and indexing to print out only the words that start with an s in this sentence:
# "Secret agents are super good at staying hidden."
string = "Secret agents are super good at staying hidden."
listofwords = string.lower().split()
print(listofwords)
for w in listofwords:
  if w[0] == 's':
    print(w)

# Using the same string as previously used:
# "Secret agents are super good at staying hidden."
# Use a for loop to only print out the words with an even number of characters/letters.

for w in listofwords:
  length = len(w)
  if length%2 == 0:
    print(w)

# Use a list comprehension to create a list of every first letter in this string:
# mystring = "Secret agents are super good at staying hidden."

list_of_first = [w[0] for w in listofwords]
print(list_of_first)

#Use list comprehension to create a list of all the even numbers from 0 to 10.
even = [n for n in range(1,11) if n%2 == 0]
print(even)

#Use the range function to create a list of all the even numbers from 0 to 10.
even2 = list(range(0,11,2))
print(even2)

#Create a for loop that uses the random library to create a list of 10 random numbers.
import random
random10 = []
for x in range(0,10):
  random10.append(random.randint(0,100))
print(random10)

#Use list comprehension and the random library to create a list of 10 random numbers
list_of_random = [random.randint(0,100) for n in range(0,10)]
print(list_of_random)

#Create a while loop that will ask the user to input an even number.
#It should keep repeating the request until an even integer is provided.
#You should only need to expect integers to be passed in, if the user provides a string or something else that can't be transformed to an integer with int(), then the loop should break with an error.
result = 3
while result%2 != 0:
  num = int(input("provide even number"))
   if num%2 != 0:
    result = 1
   else :
    print('thank you')
    result = 2


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

