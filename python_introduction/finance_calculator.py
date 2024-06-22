monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
interest_rate = 0.05
annual_savings_with_interest = monthly_savings * 12 * interest_rate
projected_savings = annual_savings + annual_savings_with_interest
monthly_savings_result = f"Your monthly savings are ${monthly_savings}"
projected_savings_result = f"Projected savings after one year, with interest, is: ${projected_savings}"
print(monthly_savings_result)
print(projected_savings_result)