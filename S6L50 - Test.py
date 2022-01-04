"""

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
    else:
        if a < b:
            return b

q = lesser_of_two_evens(2,4)
print(q)

w = lesser_of_two_evens(2,5)
print(w)

# A shorter way:

def lesser_of_two_evens2(c, d):
    if c % 2 == 0 and d % 2 == 0:
        return min(c,d)
    else:
        return max(c,d)
# - - - - - - - - - - - - - - - - - - - - -

# Are first letters are same?
def animal_crackers(text):
    devidedList = text.split()

    print(devidedList)

    return devidedList[0][0].lower() == devidedList[1][0].lower()

print(animal_crackers('Levelheaded Llama'))

print(animal_crackers('Crazy Kangaroo'))

#  - - - - - - - - - - - - - - - - - - - -
print("\nn1 & n2:")

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20:
        print("Separate: True")
    elif n1 + n2 == 20:
        print("Summ: True")
    else:
        print("False")

makes_twenty(20,0)


# OR a shorter way:
def makes_twenty2(n1,n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20

# - - - - - - - - - - - - - - - - - - - - - -


# Make 1st & 4th letter CAPITAL:
def old_macdonald(name):
    first_letter = name[0]
    gap_before3 = name[1:3]
    fourthLetter = name[3]
    rest = name[4:]
    print(first_letter.upper() + gap_before3 + fourthLetter.upper() + rest)


old_macdonald("macdonald")


# A bit better way:  lol :D Thought it wold be better to create
# a list from a string, papitalize [0]&[3] & then append them beck.

# .capitalize()  makes 1st capital & others lowercase
def old_macdonald2(name):
    fistHalf = name[:3]
    secondHalf = name[3:]
    print(fistHalf.capitalize() + secondHalf.capitalize())

old_macdonald2("macdonald")
"""

# - - - - - - - - - - - - - - - - - - - - - -

def master_yoda(text):
    yodaList1 = text.split()
    yodaList2 = yodaList1[::-1]
    yodaList3 = " ".join(yodaList2)
    print(yodaList3)


master_yoda('I am home')

# Another way:

def master_yoda2(text):
    yodaList3 = text.split()
    yodaList3.reverse()
    yodaList4 = " ".join(yodaList3)
    print(yodaList4)


master_yoda2('We are ready')

# - - - - - - - - - - - - - - - - - - - - - -
print("\n")
# abs(x) вычисляет абсолютное значение аргумента x. По аналогии функция fabs(x)
# модуля math вычисляет то же значение. Разница лишь в том, что math.fabs(x)
# возвращает число с плавающей точкой, а abs(x) вернет целое число, если
# в качестве аргумента было целое число. Fabs расшифровывается как float absolute value.


# Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

