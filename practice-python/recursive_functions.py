'''
On recursion, from Think Python 2.

A function that calls itself is recursive;

the process of executing it is called recursion.
'''

# Example 1
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

# Example 2: factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example 3: fibonacci
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
