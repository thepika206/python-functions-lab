# challenge 1 white a function named sum_to that accepts a single integer, n and returns the sum of the integers from 1 to n.

def sum_to(n):
  i=1 
  solution = 0
  while i <=n:
    solution += i
    i += 1
  return solution

# tests
print(sum_to(6))
print(sum_to(10))


# challenge 2