def lowestToHighest(list):
  return sorted(list)

print(lowestToHighest([1,3,5,7,9,2,0]))

def middleValue(listOfNb):
  sortedList = lowestToHighest(listOfNb)
  middle = float(len(listOfNb))/2
  if middle % 2 != 0:
    return sortedList[int(middle - .5)]
  else:
    return (sortedList[int(middle)] + sortedList[int(middle-1)]) / 2


print(middleValue([1,2,3,4,5]))
print(middleValue([1,2,3,4]))

# def median(listOfNb):
#   sortedList = lowestToHighest(listOfNb)











