monthly_income = float(input("Enter your monthly income:"))
monthly_expences = float(input("Enter your monthly expenses:"))
monthly_savings = monthly_income - monthly_expences
annual_savings = monthly_savings * 12 

annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

print(f"\nYour monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
