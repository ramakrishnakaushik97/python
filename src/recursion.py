# 5 * 4 * 3 * 2 * 1 = 120
# 5!
# 0! = 1
# 1! = 1


def getFactorial_recursive(n):

    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * getFactorial(n - 1)

def getFactorial_iterative(n):
  fact=1
  for i in range(1, n+1):
    fact = fact*i 
  return fact
  
print(getFactorial_recursive(5))
print(getFactorial_iterative(5))
