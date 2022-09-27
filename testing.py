def divisible_by_ten(nums):
  counter = 0
  for num in nums:
    if num % 10 == 0:
      counter += 1
    return counter

def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

def max_num(nums):
  max_val = nums[0]
  for number in nums:
    if number > max_val:
      max_val = number
  return max_val


def same_values(lst1, lst2):
  lst3 = []
  for index in range(len(lst2)):
    if lst1[index] == lst2[index]:
      lst3.append(index)
  return lst3

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
  
# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
  
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
  
for i in range(0,len(highlighted_poems_details)):
  pass
    # print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

diameter = 30

def this_function_is_an_object(name):
  return name

print(this_function_is_an_object('Lol'))

print(f"New circle with diameter: {diameter}")

import random

numbers_a = range(1, 13)
numbers_b = random.sample(numbers_a, range(1000))
print(numbers_b)

