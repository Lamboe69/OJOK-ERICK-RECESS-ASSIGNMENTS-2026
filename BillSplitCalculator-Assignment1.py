while True:
    try:
        bill_amount = float(input("Enter the total bill amount (UGX): "))
        if bill_amount <= 0:
            print("Please enter a bill amount greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a number.")

while True:
    try:
        num_people = int(input("Enter the number of people splitting the bill: "))
        if num_people <= 0:
            print("Number of people must be at least 1.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a whole number.")

print("\nChoose a tip percentage:")
print("  1. 10%")
print("  2. 15%")
print("  3. 20%")
print("  4. Custom tip")

while True:
    try:
        tip_choice = int(input("Enter your choice (1-4): "))
        if tip_choice == 1:
            tip_percent = 10
            break
        elif tip_choice == 2:
            tip_percent = 15
            break
        elif tip_choice == 3:
            tip_percent = 20
            break
        elif tip_choice == 4:
            while True:
                try:
                    tip_percent = float(input("Enter your custom tip percentage: "))
                    if tip_percent < 0:
                        print("Tip cannot be negative.")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Please enter a number.")
            break
        else:
            print("Please choose a number between 1 and 4.")
    except ValueError:
        print("Invalid input! Please enter 1, 2, 3, or 4.")

tip_amount = bill_amount * (tip_percent / 100)
total_bill = bill_amount + tip_amount
amount_per_person = total_bill / num_people

print("\n")
print("=" * 40)
print("         BILL SPLIT RECEIPT")
print("=" * 40)
print(f"  Original Bill:      UGX {bill_amount:,.2f}")
print(f"  Tip ({tip_percent}%):          UGX {tip_amount:,.2f}")
print(f"  Total Bill:         UGX {total_bill:,.2f}")
print(f"  Number of People:   {num_people}")
print("-" * 40)
print(f"  Each Person Pays:   UGX {amount_per_person:,.2f}")
print("=" * 40)
print("  Thank you! Enjoy your meal!")
print("=" * 40)
