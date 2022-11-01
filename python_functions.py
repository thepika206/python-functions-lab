# challenge 1 write a function named sum_to that accepts a single integer, n and returns the sum of the integers from 1 to n.

def sum_to(n):
  i=1 
  solution = 0
  while i <=n:
    solution += i
    i += 1
  return solution

# tests for #1
print('chall #1,  expect 21, 55')
print(sum_to(6))
print(sum_to(10))


# challenge 2 Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  nums.sort()
  return nums[-1]


# tests for #2
print('chall #2, expect 4, 231')
print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

# Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(str1, str2):
  return str1.count(str2)

# tests for #3
print('chall #3, expect 2,2,1,0')
print(occurrences('fleep floop', 'e'))   # returns 2
print(occurrences('fleep floop', 'p'))   # returns 2
print(occurrences('fleep floop', 'ee'))  # returns 1
print(occurrences('fleep floop', 'fe'))  # returns 0

# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  solution = 1
  for item in args:
    solution *= item
  return solution

# tests for #4
print('chall #4, expect -4, 50, 10.0')
print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0