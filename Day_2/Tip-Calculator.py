print('Welcome to the tip calculator!')
bill_amount = float(input('What was the total bill $? '))
tip = int(input('How much would you like to give? 10, 12 or 15?'))
split = int(input('How many people would you like to split?'))
total_bill = tip / 100 * bill_amount + bill_amount
bill_per_person = (total_bill)/ split
print(f'Each person should pay:  {bill_per_person}')
