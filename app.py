def main ():

    choice = -2
    while choice != -1:
        print("1: Select an option")
        print("2: Set monthly income")
        print("3: Set monthly rent")
        print("4: Set monthly utilities")
        print("5: Set other monthly recurring expenses")
        print("0: Save and Exit:")

        choice


    monthly_income = int(input("What is your monthly income? "))
    monthly_rent = int(input("What is your rent? "))
    other_recurring_bills = int(input("Other recurring bills? "))

    print(f"Your left over income is {monthly_income - monthly_rent - other_recurring_bills}");


if __name__ == "__main__":
    main()