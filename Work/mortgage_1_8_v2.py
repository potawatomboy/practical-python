# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
counter = 0
while principal > 0:
    if counter < 12:
        principal = principal * (1+rate/12) - payment - 1000
        total_paid = total_paid + payment + 1000
        counter = counter + 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        
print('Total paid', total_paid)

#Total paid 929965.6199999959 - first result
