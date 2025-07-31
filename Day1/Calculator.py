def tip_calculator():
    print("Welcome to the Tip Calculator!")

    try:
        bill = float(input("What was the total bill? $"))
        tip_percent = float(input("What percentage tip would you like to give? (e.g., 15, 18, 20): "))
        people = int(input("How many people to split the bill? "))

        tip_amount = (tip_percent / 100) * bill
        total_bill = bill + tip_amount
        amount_per_person = total_bill / people

        print(f"\nBill before tip: ${bill:.2f}")
        print(f"Tip amount (@{tip_percent}%): ${tip_amount:.2f}")
        print(f"Total bill with tip: ${total_bill:.2f}")
        print(f"Each person should pay: ${amount_per_person:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        print("Number of people must be at least 1.")

# Run the calculator
tip_calculator()
