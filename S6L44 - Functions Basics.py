
def say_hello():
    print("Hello, ")
    print("do you ")
    print("like Cheese ?")

say_hello()
# Hello,
# do you
# like Cheese ?


print("\n")

def say_hi(_name):
    print(f"Hi, {_name}")

say_hi("Jose")
# Hi, Jose

print("\n")

# If "Jose" is missing, an Error will occure.
# The way to avoid it: put a default value

def greet(_name = "Robot"):
    print(f"Hi, {_name}")

greet()
# Hi, Robot


print("\n")

# Return:
def add_num(num1, num2):
    return(num1 + num2) #Brackets are not necessary

result = add_num(10,20)
print(result)
# 30


# Print & return can be used both. One after another.
