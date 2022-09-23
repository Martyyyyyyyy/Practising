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
