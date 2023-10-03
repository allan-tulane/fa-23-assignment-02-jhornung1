"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def subquadratic_multiply(x, y, memo={}):
    # Base case: If either x or y has a length of 1 (basically either a 1 or a 0), 
    # return the multiple
    if len(x.binary_vec) == 1 or len(y.binary_vec) == 1:
        return x.decimal_val * y.decimal_val

    # Check if the result is already memoized. This is to solve the recursion problems 
    # I was having with b = on line 70
    if (x.decimal_val, y.decimal_val) in memo:
        return memo[(x.decimal_val, y.decimal_val)]

    # Convert x and y to binary vectors of equal length
    x_vec, y_vec = pad(x.binary_vec, y.binary_vec)

    # Calculate the number of bits in x_vec (which is the same length as y_vec)
    n = len(x_vec)

    # Divide x and y into two equal halves
    x_high, x_low = split_number(x_vec)
    y_high, y_low = split_number(y_vec)

    # Recursively calculate the products for the three subquadratic values in Karatsuba 
    # formula
    a = subquadratic_multiply(x_high, y_high, memo)
    b = subquadratic_multiply(x_low, y_low, memo)

    x_mod = x_high.decimal_val + x_low.decimal_val
    y_mod = y_high.decimal_val + y_low.decimal_val

    newX = BinaryNumber(x_mod)
    newY = BinaryNumber(y_mod)

    c = subquadratic_multiply(newX, newY, memo)

    # Calculate the result using the Karatsuba multiplication formula
    result = (a << n) + ((c - a - b) << (n // 2)) + b

    # Memoize the result as a permanent save
    memo[(x.decimal_val, y.decimal_val)] = result

    return result

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

