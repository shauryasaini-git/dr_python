import csv
import os   # lets us check things about the filesystem, like whether a file exists
from sys import exit


#rename the file we only change it in one place
DATABASE_FILE = "database.csv"
PATIENTS_FILE = "patients.csv"

def ensure_trailing_newline(path):
    # csv writer assumes it starts on a fresh line; without this, appending
    # to a file whose last line lacks a newline jams the new row onto it.
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "rb") as file:
            file.seek(-1, os.SEEK_END)
            last_byte = file.read(1)

        if last_byte != b"\n":
            with open(path, "a", newline = "", encoding = "utf-8") as file:
                file.write("\n")

def sign_up():
    name = input("Enter your name: ")
    number = input("Enter your number: ")
    mail = input("Enter your mail: ")

    file_exists = os.path.exists(DATABASE_FILE) and os.path.getsize(DATABASE_FILE) > 0
    ensure_trailing_newline(DATABASE_FILE)

    # newline="" is recommended by Python's csv docs to avoid extra blank
    # lines / broken line endings on Windows.
    with open(DATABASE_FILE, "a", newline = "", encoding = "utf-8") as file:
        # DictWriter lets us write rows using a dict with named keys
        writer = csv.DictWriter(file, fieldnames = ["name", "number", "mail"])

        if not file_exists:
            writer.writeheader()

        writer.writerow({"name" : name, "number" : number, "mail" : mail})

    print("Sign up successful")

def sign_in():
    number = input("Enter your number to sign back in: ")
    found = False

    if not os.path.exists(DATABASE_FILE):
        print("No user in the database`1")
        exit(1)

    with open(DATABASE_FILE, "r", encoding = "utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            #row.get("number", "") is safer
            if row.get("number", "").strip() == number.strip():
                found = True
                print("Welcome back")

    if not found:
        print("User not found, please sign up first")

def main():
    while True:
        choice = input("Sign_in, Sign_up, or Exit: ").strip().lower()

        if choice == "sign_up":
            sign_up()
        elif choice == "sign_in":
            sign_in()
        elif choice == "exit":
            print("Goodbye")
            break
        else:
            print("Invalid choice, please enter Sign_in, Sign_up, or Exit")
            continue

        #now comes the homepage
        while True:
            patient_name = input("Patient's name(N to exit): ")
            
            if patient_name == "N":
                print("Exiting!")
                exit(0)

            prescription = input("Prescription: ")
            date = input("Date: ")

            try:
                fee = int(input("fee(only numerical value): "))
            except ValueError:
                print("Invalid input for fee! Please enter a number.")
                continue

            file_exists = os.path.exists(PATIENTS_FILE) and os.path.getsize(PATIENTS_FILE) > 0
            ensure_trailing_newline(PATIENTS_FILE)

            with open(PATIENTS_FILE, "a", newline = "", encoding = "utf-8") as file:
                writer = csv.DictWriter(file, fieldnames = ["name", "prescription", "date", "fee"])

                if not file_exists:
                    writer.writeheader()

                writer.writerow({"name" : patient_name, "prescription" : prescription, "date" : date, "fee": fee})

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
        exit(0)
