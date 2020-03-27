# Checks if the entered Credit Card number is valid or not!

# Sample Credit Card numbersCredit Card
# Visa  	4111 1111 1111 1111
# MasterCard  	5500 0000 0000 0004
# American Express  	3400 0000 0000 009
# Diner's Club  	3000 0000 0000 04
# Carte Blanche  	3000 0000 0000 04
# Discover  	6011 0000 0000 0004
# en Route  	2014 0000 0000 009
# JCB  	3088 0000 0000 0009

# Input of credit card number
card_no = input("Enter Credit Card number to validate(no spaces): ")

# Splitting to list
num = card_no.split()

# Luhn's Algorithm ####
n = -1 * len(num)
j = -2
l1 = list()
while j > n:
    l1.append(int(num[-2])*2)
    j -= 2
sum = 0
k = -1

while k > n:
    sum += int(num[k])
    k -= 2

for i in l1:
    if i < 10 == 0:
        sum += i
    else:
        sum += i % 10 + i // 10

if sum % 10 == 0:
    print("Entered Credit Card number is Valid!")
else:
    print("Entered Credit Card number is NOT Valid!")
