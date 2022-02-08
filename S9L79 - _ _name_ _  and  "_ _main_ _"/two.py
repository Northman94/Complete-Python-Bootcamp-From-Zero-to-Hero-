# Usually:  from A import B

import one

print("Highest Level in Two.py")

one.func()


if __name__ == "__main__":
    # RUN THE SCRIPT!
    print("Two.py is being Run directly.")
else:
    print("Two.py had been imported.")

