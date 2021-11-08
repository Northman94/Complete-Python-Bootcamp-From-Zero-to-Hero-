
stock_prices = [("APPL", 200),("GOOG",400),("MSFT",100)]

for item in stock_prices:
    print(item)
# ('APPL', 200)
# ('GOOG', 400)
# ('MSFT', 100)


for ticker,price in stock_prices:
    print(ticker)

# APPL
# GOOG
# MSFT


for ticker,price in stock_prices:
    print(price)

# 200
# 400
# 100


work_hours = [("Abby",400),("Billy",200),("Cassie",800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = " "

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # Return
    return (employee_of_month, current_max)


result = employee_check(work_hours)

print(result)
# ('Cassie', 800)


# OR:


name,hours = employee_check(work_hours)

print(name)
print(hours)

# Cassie
# 800
