
myString = "Hello World"

myString[5]
# Will return Space " "

myString[6]
# Will return "W"

myString[-2]
# Will return "l"


# Slicing:

myString2 = "ABCDEFGH"

myString2[:3]
# Will return 'ABC'

myString2[3:]
# Will return 'DEFGH'

myString2[3:6]
# Will return 'DEF'


# myString2 & myString2[ : : ] both returning full string

myString2[3:-3]
# Will return 'DE'


# [0] is always included in jumping over.

myString2[::2]
# Will return 'ACEG'

myString2[::3]
# Will return 'ADG'


# Reversing string:
myString2[::-1]
# Will return'HGFEDCBA'


"ABCDEFGH"[2]
# Will return  'C'
