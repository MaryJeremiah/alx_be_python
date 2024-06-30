monthly_income = int(input('Enter your monthly_income:'))
monthly_expenses = int(input('Enter you total monthly expenses:'))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings *12 + (monthly_savings*12*0.06)
print('Your monthly savings are', monthly_savings)
print('Projected savings after one year, with interest, is:', projected_savings)

#define variables
monthly_income = 5000
total_monthly_expenses = 4000
monthly_savings = 1000
Projected_savings_after_one_year, with_interest = 12600
