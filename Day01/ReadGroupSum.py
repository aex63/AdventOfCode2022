# Initial documentation
'''
= Date: 2022-12-01
= Title/Project: AdventOfCode (Day 1)
= Description: Coding exercise one - Calculate data regarding group of elfs and their available calories
= Author: Aex63/Leonard
= Github: @aex63
'''

# Import essential functions from python to process and work with data
import os, heapq

# Define current location and input file location
current_directory = os.path.realpath(os.path.dirname(__file__))
IOFile = current_directory + '\\' + 'input.txt'

# Empty list to build raw data for all elf groups
groups = []
  
# Open input file and read formated lines into variable to work with
with open(IOFile) as f:
    li = [l.strip() for l in f.readlines()]

# Temprorary empty list to dump items into from the for-loop
templist = []

# Loop through all lines in the file and only add numerical values into templist
# For every new non-numerical line: dump templist into groups so that we group all the calories into set groups
# Then reset the templist and keep iterating through the list 
for i in range(len(li)):
    if i < len(li)-1:
        # Until end is reached
        if li[i].isnumeric():
            templist.append(li[i])
        else:
            groups.append(templist)
            templist = []

    else:
        # End
        templist.append(li[i])
        groups.append(templist)
        templist = [] 

# Dictionary with all the grouped data
elfGroups = {}

# Convert the list into a dictionary
count = 0
for item in groups:
        count += 1
        elfGroups["{}".format(count)] = item

# Create the final list for processing data from the elfs
datalist = []

# For every group and set of calories in dictionary: iterate through the data to add one dictionary for every key-pair together with a total sum
for group, calories in elfGroups.items():
    total = 0
    for ele in range(0, len(calories)):
        total = total + int(calories[ele])
    newItem = {'Group': group,'Calories': calories,'Sum': total}
    datalist.append(newItem)

# Lambda inline function to extract INT values from list of dictionaries
getValuesINT = lambda key,inputData: [int(subVal[key]) for subVal in inputData if key in subVal]

# Function to extract MAX value from key in list-dictionary
def MaxValueFromListOfDicts(key, list):
    maxcalories = max(getValuesINT(key, list))
    return maxcalories 

# Function to extract TOP x largest values from key in list-dictionary
# Using Heapq algorithm (binary trees): https://docs.python.org/3/library/heapq.html
def TopValuesFromListOfDicts(key, list, top):
    """
    HeapQ Useful code (TOP 2)
        print('Largest:', heapq.nlargest(2, sumlist))
        print('Smallest:', heapq.nsmallest(2, sumlist))
    """
    intValues = getValuesINT(key, list)
    return heapq.nlargest(top, intValues)

# Output variables for AdventOfCode Questions
maxVal = MaxValueFromListOfDicts('Sum', datalist)
topVals = TopValuesFromListOfDicts('Sum', datalist, 3)

# Answersheet to programming excercises
print(
    'Question 1: ','Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? ',
        'Answer: ', maxVal, '\n',
    'Question 2: ','Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total? ',
        'Answer: ', sum(topVals),
    sep='' # Disable the softspace feature
)