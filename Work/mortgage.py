# mortgage.py
#
# Exercise 1.7

mortgage_period = 0
mortgage_percent = 0.05
mortgage_amount = 500000
monthly_payment = 2684.11

total_paid = 0
while mortgage_amount > 0:

    if mortgage_period < 12:
        mortgage_amount = mortgage_amount * (1 + mortgage_percent / 12) - (monthly_payment + 1000)
        total_paid += monthly_payment + 1000
    else:
        mortgage_amount = mortgage_amount * (1 + mortgage_percent / 12) - monthly_payment
        total_paid += monthly_payment

    mortgage_period += 1

print(round(total_paid, 2), mortgage_period)
    