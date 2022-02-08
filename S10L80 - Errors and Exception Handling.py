
# A way to get an error type:
try:
    a = 2 + "a"
except Exception as e:
    print(e)
# unsupported operand type(s) for +: 'int' and 'str'






try:
    result = 10 + '10'
except:
    print("Addition Error")
else:
    # If there is no Exception.
    print("All good.")
    print(result)
# Addition Error




try:
    f = open('S10L80_file','w')
    f.write("Write a Test Line")
except TypeError:
    print("A Type Error")
except OSError:
    print("An OS Error. Writing to read-only file") # r
finally:
    print("Always Run.")
# Always Run.




def ask_for_int():
    while True:
        try:
            res = int(input("Pls provide a Numb: "))
        except:
            print("Not a Number.")
        else:
            print("Ok, thanks.")
            break
        finally:
            print("Always run in the End.")

# Recommends not to mix else + break with finally. Choose ont of those.
# But it can be both.

ask_for_int()
# Pls provide a Numb: A
# Not a Number.
# Always run in the End.

# Pls provide a Numb: 4
# Ok, thanks.
# Always run in the End.
