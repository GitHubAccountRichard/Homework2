while True:
    try:
        gross_income = float(input("Please enter a valid gross income: "))
        Num_Kids = int(input("Please enter the number of kids you have: "))
        if gross_income > 0 and Num_Kids >= 0:
            break
    except ValueError:
        print("Please enter a valid number.")
if gross_income < 1000:
    net_income = gross_income * (1-(0.1-Num_Kids*0.01))
elif gross_income < 2000:
    net_income = gross_income * (1-(0.12-Num_Kids*0.01))
elif gross_income < 4000:
    net_income = gross_income * (1-(0.14-Num_Kids*0.005))
else:
    net_income = gross_income * (1-(0.18-Num_Kids*0.005))
print(f"Your net income is: {net_income}")