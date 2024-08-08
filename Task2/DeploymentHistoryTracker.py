import datetime
import os

from Record import Record
from App import App

records = {}
path = None
file = None

#  Validations: date, version, environment, developer, name:
# ==========================================================


def is_file_empty():
    try:
        if os.stat(path).st_size == 0:
            return True
    except Exception:
        return False


def is_file_valid():
    return path.endswith(".txt")


def if_file_exists():
    return os.path.exists(path)


def is_date_valid(date):
    if date is None:
        return False
    date = date.strip()
    now = datetime.datetime.now()
    try:
        year, month, day = date.split("-")
        date = datetime.datetime(int(year), int(month), int(day))
    except Exception:
        return False
    else:
        return date <= now


def is_version_valid(version):
    version = version.strip()
    try:
        version = version.split(".")
        for v in version:
            if not v.isdigit():
                return False
        if len(version) >3 or len(version) < 1:
            return False
    except Exception:
        return False
    else:
        return float(version[0]) > 0


def is_environment_valid(environment):
    environment = environment.strip()
    return environment != ""


def is_developer_valid(developer):
    developer = developer.strip()
    return developer != ""


def is_name_valid(name):
    name = name.strip()
    return name != ""


def is_record_valid(record):
    if record is None:
        return False
    try:
        name, environment, version, date, developer = record.split(",")
    except ValueError:
        return False
    else:
        return is_name_valid(name) and is_environment_valid(environment) and is_version_valid(version) and is_date_valid(date) and is_developer_valid(developer)

# ==========================================================
#  End of Validations

def validate_date(date_string):
    try:
        year, month, day = date_string.split("-")
        date = datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        print(f"error happened in date: {date_string}, should be a valid yyyy-mm-dd")
        while True:
            choice = input("Chose a solution: 1.Continue with today`s date 2.Enter a date again 3. Skip line:")
            if choice == "1":
                date = datetime.datetime.now()
                return date.date()
            elif choice == "2":
                new_date_string = input("Enter the date again: ")
                return validate_date(new_date_string)
            else:
                return None
    return date.date()


def validate_record_line(line):
    try:
        name, environment, version, date, developer = line.split(",")
        if len(line.split(",")) != 5:
            return None
    except ValueError:
        return None
    if is_name_valid(name.strip()) and is_developer_valid(developer) and is_environment_valid(environment) and is_version_valid(version):
        if not is_date_valid(date):
            return None
        record = Record(name, environment, version, date, developer)
        return record

    if name == "" and environment == "" and version == "" and developer == "":
        # end of the file
        return None
    else:
        print(f"error in record: {line}, should be a valid record")
        print("1. Enter the record again")
        print("2. Skip the record")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("The format of the record should be: name,environment,version,yyyy-mm-dd,developer")
            new_line = input("Enter the record again: ")
            new_record = validate_record_line(new_line)
            if new_record is None:
                print("Your input record is invalid too, discarded")
            return new_record
        else:
            return None


def insert_record(record):
    # Add the valid record to the dic (records)
    key = App(record.app_name, record.version, record.environment).info()
    value = record
    records[key] = value


# Read all the records from the file
# and add them to the records-dictionary after validation
def read_all_records():
    global path
    global file
    with open(path, "r") as file:
        file.readline()
        for line in file:
            record = validate_record_line(line)
            if record is not None:
                insert_record(record)

# Functionalities:
# ==========================================================
def add_record():
    print("Adding a record:")
    app_name = input("Enter app name: ")
    if is_name_valid(app_name):
        version = input("Enter version: ")
        if is_version_valid(version):
            environment = input("Enter environment: ")
            if is_environment_valid(environment):
                key = App(app_name, version, environment).info()
                if records.get(key):
                    print("This record already exists")
                    return

                date = input("Enter date: ")
                date = validate_date(date)
                if date is not None:
                    developer = input("Enter developer: ")+"\n"
                    if is_developer_valid(developer):
                        record = Record(app_name, environment, version, date, developer)
                        insert_record(record)
                        print("Record added successfully")
                        return
    print("Record is not valid, Discarded")


def update_record():
    print("Enter the App name and version to update information")
    name = input("Enter the App name: ")
    version = input("Enter the version: ")
    environment = input("Enter the environment: ")
    key = App(name, version, environment).info()
    if records.get(key):
        print(f"The old information is: {records[key].info()}")
        date = input("Enter the new date: ")
        date = validate_date(date)
        if date is not None:
            developer = input("Enter the new developer: ")
            if is_developer_valid(developer):
                rec = records[key]
                rec.version = version
                rec.date = date
                rec.developer = developer
                rec.environment = environment
                print("Record is updated successfully")
                return
            else:
                print("Developer is not valid, Discarded")
                return
        else:
            print("Date is not valid, Discarded")
            return
    else:
        print("No Deployment is found with this specs")


def display_all_records():
    for key in records:
        print(records[key].info())


def save_in_new_file():
    global path
    # write on a new file
    try:
        now = datetime.datetime.now()
        new_file_name = "./result_" + str(now.time()) + ".csv"
        new_file = open(new_file_name, "w+")
        new_file.seek(0)
    except Exception:
        print("Error happened while writing to the file")
        return
    new_file.write("App Name,Environment,Version,Deployment Date,Deployed by\n")
    for key in records:
        new_file.write(records[key].info())
    new_file.close()
    print(f"File is saved in {new_file_name} successfully")


def overwrite_file():
    global path
    global file
    with open(path, "w") as file:
        file.write("App Name,Environment,Version,Deployment Date,Deployed by\n")
        for key in records:
            file.write(records[key].info())
        print("File is overwritten successfully")


# ==========================================================

# startup functions
# ==========================================================


def read_and_validate_file():
    global file
    global path
    while True:
        path = input("Enter file path to start: ")
        if all([if_file_exists(), is_file_valid(), not is_file_empty()]):
            try:
                file = open(path, "r+")
                file.seek(0)
            except Exception:
                print("Not a correct path/file name")
                continue
            else:
                break
            finally:
                file.close()
                pass

def printMenu():
    print("\nEnter your choice for next step: ")
    print("1. Display all records")
    print("2. Add a record")
    print("3. Update a record")
    print("4. Save in a new file")
    print("5. Overwrite the same file")
    print("6. Exit ")


def main():
    global records
    global path
    print("This is a deployment history tracker")
    read_and_validate_file()
    read_all_records()
    if len(records) > 0:
        print("All records are read and validated")
        printMenu()
        choice = input(":")
        while choice != "6":
            if choice == "1":
                display_all_records()
            elif choice == "2":
                add_record()
            elif choice == "3":
                update_record()
            elif choice == "4":
                save_in_new_file()
            elif choice == "5":
                overwrite_file()
            else:
                print("Invalid choice :?")
            printMenu()
            choice = input(":")
    else:
        print("No records are found in the file, (File is empty)")
        print("Exiting the program")

# ==========================================================
#  Start the program


main()
