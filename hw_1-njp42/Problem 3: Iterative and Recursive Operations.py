# Write an iterative function and a recursive function that computes the sum of
# all numbers from 1 to n, where n is given as parameter.

# Iterative
def iterative(n):
    x = 0
    for i in range(1, n+1):
        x = i + x
    return x

# Recursive
def recursive(n):
    if n == 0:
        return 0
    else:
        return n + recursive(n-1)

print(iterative(100), recursive(100))
