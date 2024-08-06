import datetime
from Record import Record
from App import App

records = {}
path = None
file = None


def validate_date(date_string):
    try:
        year, month, day = date_string.split("-")
        date = datetime.datetime(int(year), int(month), int(day))
    except Exception:
        print(f"error happened in date: {date_string}, should be a valid yyyy-mm-dd")
        while True:
            choice = input("Chose a solution: 1.Continue with today`s date 2.Enter a date again 3. Skip line:")
            if choice == 1:
                date = datetime.datetime.now()
                break
            elif choice ==2:
                date_string = input("Enter the date again: ")
                return validate_date(date_string)
            else:
                date = None
                break
        pass
    else:
        return date.date()
    pass


def validate_record(line):
    name, environment, version, date, developer = line.split(",")
    if name != "" and environment != "" and version != "" and developer != "":
        date = validate_date(date)
        if date is None:
            return None
        record = Record(name, environment, version, date, developer)
        return record
    else:
        if name == "" and environment == "" and version == "" and developer == "":
            # end of the file
            return None
        else:
            print(f"error happened in record: {line}, should be a valid record")
            print("1. Enter the record again")
            print("2. Skip the record")
            choice = input("Enter your choice: ")
            if choice == 1:
                line = input("Enter the record again: ")
                return validate_record(line)
            else:
                return None
        pass
    pass


def add_record(record):
    # Add the valid record to the dic (records)
    key = App(record.app_name, record.version).info()
    value = record+"\n"
    records[key] = value
    pass


# Read all the records from the file
# and add them to the records dictionary after validation
def read_all_records():
    for line in file:
        record = validate_record(line)
        if record is not None:
            add_record(record)
    pass


def update_record():
    print("Enter the App name and version to update information")
    name = input("Enter the App name: ")
    version = input("Enter the version: ")
    key = App(name, version).info()
    if records.get(key):
        print(f"The old information is: {records[key].info()}")
        line = input("Enter the new information: ")
        record = validate_record(line)
        if record is not None:
            records[key] = record
        else:
            print("Record is not valid, it stays the same")
    else:
        print("No app is found with this specs")
    pass


def display_all_records():
    for key in records:
        print(records[key].info())


def read_validate_file():
    global file
    while True:
        path = input("Enter file path to start: ")
        try:
            file = open(path, "r")
            file.seek(0)
        except Exception:
            print("Not a correct path/file name")
            continue
        else:
            break
    pass


def save_in_new_file():
    global path
    new_path = input("Enter the new file path: ")
    new_file = open(new_path, "w+")
    for key in records:
        new_file.write(records[key].info())
    new_file.close()
    pass


def overwrite_file():
    global path
    try:
        for key in records:
            file.write(records[key].info())
        file.close()
    except Exception:
        print("Error happened while writing to the file")
    pass


def printMenu():
    print("Enter your choice for next step: ")
    print("1. Display all records")
    print("2. Add a record")
    print("3. Update a record")
    print("4. Save in a new file")
    print("5. Overwrite the same file")
    print("6. Exit ")
    pass


def main():
    global records
    global path
    print("This is a deployment history tracker")
    read_validate_file()
    read_all_records()
    if len(records) > 0 :
        print("All records are read and validated")
        printMenu()
        choice = input(":")
        while choice != "6":
            if choice == "1":
                display_all_records()
            elif choice == "2":
                record = input("Enter the record: ")
                try:
                    record = validate_record(record)
                except ValueError:
                    record = None
                    print("Not a valid record")
                if record is not None:
                    add_record(record)
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
    pass


main()
