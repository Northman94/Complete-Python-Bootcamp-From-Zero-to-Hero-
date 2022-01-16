'''

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

# - - - - - - - - - - - - - - - - - - - - - -

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere

# Length counts from 1
# Range - from 0

def has_33(nums):
    n = 0
    lstLength = len(nums)  # 4

    for x in range(lstLength - 1):  # range(from 0 to 2)
        first = nums[0 + n]
        second = nums[1 + n]
        print(f"F: {first}")
        print(f"S: {second}")

        if first == second:
            print("True \n")
            break
        elif n == lstLength - 2:
            print("False")
            break
        else:
            n += 1

has_33([1, 2, 3, 3])
has_33([1, 3, 1, 3])

# MISTAKES:
# No need to create an external iterator n;
# No need to create compared variables separately;
# No need to break, if you can return;

# A better way:

def has_3_3(nums2):
    for x1 in range(0, len(nums2) - 1):
        if nums2[x1] == nums2[x1+1]:
            return True
    return False

print(has_3_3([1, 3, 3, 1]))
print(has_3_3([1, 3, 1, 3]))

# Another way (number 3 specific):

def has_3_3(nums3):
    for p in range(0, len(nums3) - 1):
        if nums3[p:p+2] == [3, 3]:
            return True
    return  False

# - - - - - - - - - - - - - - - - - - - - - -


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

text_split = []
text_merge = []

def paper_doll(text):
    for elm in text:
        text_split.append(elm * 3)

    text_merge = "".join(text_split)
    print(text_merge)


# A Shorter Way:

def paper_doll2(text):
    result = ''

    for char in text:
        result += char * 3
    return result



# BLACKJACK: Given three integers between 1 and 11, if their sum
# is (less than or equal to 21), return their sum. If their sum
# (exceeds 21) *and* there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

# First Try:
def blackjack(a, b, c):
    summ = a + b + c

    if summ <= 21:
        return summ
    elif summ > 21 and a == 11 or b == 11 or c == 11:
        adjustment = summ - 10

        if adjustment > 21:
            print("BUST")
        else:
            return adjustment
    else:
        print("BUST")

# Manged to simplify:

def blackjack2(a, b, c):
    summ = (a + b + c)
    adjustment = summ - 10

    if summ > 21:
        if adjustment > 21 and a == 11 or b == 11 or c == 11:
            return adjustment
        else:
            print("BUST")
    else:
        return summ

blackjack2(5,6,7) # --> 18
blackjack(9,9,9)  #--> 'BUST'
blackjack(9,9,11) # --> 19


# Teacher:
def blackjack3(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31: # OR sum([a,b,c])-10 <= 21:
        return sum([a,b,c])-10
    else:
        return "BUST"

# - - - - - - - - - - - - - - - - - -
'''
# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending
# to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.

def summer_69(arr):
    excludedList = []

    for v in arr:
        if 5 < v and v < 10:
            continue
        else:
            excludedList.append(v)

    return sum(excludedList)


summer_69([1, 3, 5]) #--> 9
summer_69([4, 5, 6, 7, 8, 9]) #--> 9
summer_69([2, 1, 6, 9, 11]) #--> 14

# Variation by teacher:

def summer_69_2(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False

        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

# - - - - - - - - - - - - - - - - - -



