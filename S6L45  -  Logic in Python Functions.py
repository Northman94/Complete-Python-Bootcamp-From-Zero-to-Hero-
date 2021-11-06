
def even_check(numb):
    result = numb % 2 == 0
    return result

even_check(20)
# True

even_check(21)
# False


# Better Way:

def is_even(numb2):
    return numb2 % 2 == 0

is_even(4)
# True


# RETURN TRUE IF ANY NUMB IS EVEN INSIDE A LIST

def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
            """Placeholder for not doing anything"""

check_even_list([1,3,5])
# Nothing is returned


check_even_list([2,4,5])
# True

check_even_list([5,8,9])
# True


# Common Mistake:

def check_even_lst(num_list):
    for numb in num_list:
        if numb % 2 == 0:
            return True
        else:
            return False  # WRONG !!!

check_even_lst([1,2,5])
# False

# Mistake is that it is checking only the First Numb ^^^

# I guess this simply means that the for-loop will only
# return something when loop is finished.
# Will not return something different on every iteration.


# (False) will be here:

def check_even_lst2(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass

    return False

check_even_lst2([1,2,5])
# True

check_even_lst2([1,3,5])
# False


# Return ALL even Numbs is a List:

def check_even_lst3(num_list):

    even_numbers = []
# Position makes sence because initialization
# will happen after Function call.

    for num5 in num_list:
        if num5 % 2 == 0:
            even_numbers.append(num5)
        else:
            pass

    return even_numbers


check_even_lst3([1,2,3,4,5])
# [2,4]
