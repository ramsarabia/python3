#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip_percent = int(input("What percentage would you like to give? (ie 10, 15, 20)? "))
people_splitting = int(input("How many people are splitting the bill? "))
tip_percent =  tip_percent + 100
bill_andTip = bill * (tip_percent / 100)
per_person = bill_andTip / people_splitting
per_person = round(per_person, 2)
per_person = "{:.2f}".format(per_person)
print(f"Each person should pay: ${per_person}")
