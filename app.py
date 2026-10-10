import json
import sys

DATA_FILE = "budget_users_data.json"

def load_user_data():
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_user_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def main ():

    users_data = load_user_data()

    username = input("Enter username: ").strip().lower()
    if username in users_data:
        print(f"Hello {username}")
        data = users_data[username]
    else:
        print(f"New user, {username}")
        data = {"income": 0, "rent": 0, "utilities": 0, "other": 0}

    while True:
        print(" - Select an option - ")
        print("1: Set monthly income")
        print("2: Set monthly rent")
        print("3: Set monthly utilities")
        print("4: Set other monthly recurring expenses")
        print("5: Display data")
        print("0: Save and Exit:")

        choice = int(input("choice > "))

        match choice:
            case 1:
                data["income"] = int(input("What is your monthly income? "))
            case 2:
                data["rent"] = int(input("What is your rent? "))
            case 3: 
                data["utilities"] = int(input("What is your monthly utilities? "))
            case 4:
                data["other"] = int(input("How much are other monthly recurring bills? "))
            case 5:
                print(data)
            case 0:
                left_over = data["income"] - data["rent"] - data["utilities"] - data["other"]
                print(f"Your left over income is {left_over}")
                users_data[username] = data
                save_user_data(users_data)
                sys.exit()
            case _:
                print("Not a valid option")

if __name__ == "__main__":
    main()