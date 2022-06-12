
# Hexadecimal
# Using the function hex() you can convert numbers into a hexadecimal format:

hex(246)
# '0xf6'

hex(512)
# '0x200'



# Binary
# Using the function bin() you can convert numbers into their binary format.

bin(0)
#'0b0'

bin(1)
#'0b1'

bin(-1)
#'-0b1'

bin(2)
#'0b10'

bin(32)
#'0b100000'

bin(64)
#'0b1000000'

bin(1234)
#'0b10011010010'

bin(128)
#'0b10000000'

bin(512)
#'0b1000000000'



# Exponentials
# The function pow() takes two arguments, equivalent to x^y.
# With three arguments it is equivalent to (x^y)%z, but may be more efficient for long integers.

pow(3,4)  #same as  3**4, but function is more efficient
# 81

pow(3,4,5)  #3rd numb is a Modulus
# 1


# Absolute Value.
# The function abs() returns the absolute value of a number.
# The argument may be an integer or a floating point number.
# If the argument is a complex number, its magnitude is returned.

abs(-3.14)
# 3.14

abs(5)
# 5


# Round
# The function round() will round a number to a given precision
# in decimal digits (default 0 digits). It does not convert integers to floats.

round(3.4)
# 3


# Will round to an Even Numb:
round(3.5)
# 4

round(4.5)
# 4


round(395,-2)
# 400


round(3.1415926535,2)
# 3.14


# MATH  LIBRARY  —  https://docs.python.org/3/library/math.html

