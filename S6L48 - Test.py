
# The parameter weekday is True if it is a weekday,
# and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.

# Check this cases:

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True


# My variation:
def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
       return True
    else:
      return False


# Educators variation:
def sleep_in2(weekday, vacation):
  if not weekday or vacation:    # if (w)False or (v)True
    return True
  else:
    return False


# 3rd variation:
def sleep_in3(weekday, vacation):
    return not weekday or vacation



false_false = sleep_in(False, False)
print(f"{false_false}  \n")
# False

true_false = sleep_in(True, False)
print(f"{true_false}  \n")
# False

false_true = sleep_in(False, True)
print(f"{false_true}  \n")
# False

true_true = sleep_in(True, True)
print(f"{true_true}  \n")
# False

