print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give (%)? "))
people = int(input("How many people to split the bill? "))

if people == 0:
    print("Number of people cannot be zero.")
else:
    bill_with_tip = tip / 100 * bill + bill
    bill_per_person = bill_with_tip / people
    final_amount = round(bill_per_person, 2)
    print(f"Each person pays: ${final_amount:.2f}")
