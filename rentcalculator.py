##Inputs we need from the user
#Total rent
#Total food ordered for snacking
#Electricity units spend
#charge per unit

##Output
#total amount you've to pay is

rent = int(input("Enter your rent\n"))
food = int(input("Enter the food you have ordered for snacking\n"))
electricity_bill = int(input("Enter the electricity bill\n"))
charge_unit = int(input("Enter the charge per unit\n"))
persons = int(input("Enter the number of persons in one room\n"))
total_bill = electricity_bill * charge_unit
total_amt = (rent+food+total_bill )// persons
print(f" Each person have to be payed : {total_amt}")

