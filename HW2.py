try:
    GrossSalary = float(input("Enter your gross salary: "))
    if GrossSalary < 1000:
        Income_Tax = 0.10
    elif 1000 <= GrossSalary < 2000:
        Income_Tax = 0.12
    elif 2000 <= GrossSalary < 4000:
        Income_Tax = 0.14
    else:
        Income_Tax = 0.18
except ValueError:
    print("Please enter a valid number")
try:
    Num_Children = int(input(f"Your Gross Income places you in a tax bracket with {Income_Tax} income tax, how many children do you have? "))
    if Income_Tax == 0.1 or Income_Tax == 0.12:
        Tax_Cut = 0.01
        Income_Tax_Child = Income_Tax - (0.01 * Num_Children)
    else:
        Tax_Cut = 0.005
        Income_Tax_Child = Income_Tax - (0.005 * Num_Children)
        print(Income_Tax_Child)
except ValueError:
    print("Please enter a valid number")
net_income = GrossSalary * (1-Income_Tax_Child)
print(f"Your net income is: {net_income}")