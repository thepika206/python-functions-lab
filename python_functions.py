# challenge 1 write a function named sum_to that accepts a single integer, n and returns the sum of the integers from 1 to n.

def sum_to(n):
  i=1 
  solution = 0
  while i <=n:
    solution += i
    i += 1
  return solution

# tests
print('chall #1 tests, expect 21, 55')
print(sum_to(6))
print(sum_to(10))


# challenge 2 Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  nums.sort()
  return nums[-1]


# tests
print('chall #2, expect 4, 231')
print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

