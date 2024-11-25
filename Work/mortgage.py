# mortgage.py
#
# Exercise 1.7

mortgage_period = 0
mortgage_percent = 0.05
mortgage_amount = 500000
monthly_payment = 2684.11

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

total_paid = 0
while mortgage_amount > 0:

    if mortgage_period >= extra_payment_start_month and mortgage_period <= extra_payment_end_month:
        mortgage_amount = mortgage_amount * (1 + mortgage_percent / 12) - (monthly_payment + extra_payment)
        total_paid += monthly_payment + extra_payment
    else:
        mortgage_amount = mortgage_amount * (1 + mortgage_percent / 12) - monthly_payment
        total_paid += monthly_payment

    over_payment = 0
    if mortgage_amount < 0:
        over_payment = -mortgage_amount
        mortgage_amount = 0
        total_paid -= over_payment

    mortgage_period += 1
    print(mortgage_period, round(total_paid, 2), round(mortgage_amount, 2))

# print(round(total_paid, 2), mortgage_period)
    