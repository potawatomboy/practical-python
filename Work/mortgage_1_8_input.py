# mortgage.py
# user input
# Exercise 1.8
extra_payment_start_month = int(input('Enter start month for extra payment: '))
extra_payment_end_month = int(input('Enter end month for extra payment: '))
extra_payment = int(input('Enter extra payment: '))
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
counter = 1
while principal > 0:
    if counter >= extra_payment_start_month and counter <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        counter = counter + 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        
print('Total paid', total_paid)

#Total paid 929965.6199999959 - first result
