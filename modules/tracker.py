import json
from datetime import datetime

def menu():
    print("▶︎ Choose an option:")
    print("[1] Log Income")
    print("[2] Log Strategy")
    print("[3] Log Donation")
    choice = input("Enter: ")

    if choice == "1":
        log_income()
    elif choice == "2":
        log_strategy()
    elif choice == "3":
        log_donation()

def log_income():
    source = input("Source (e.g. Toloka): ")
    amount = input("Amount (৳): ")
    note = input("Note: ")
    entry = {
        "date": str(datetime.now()),
        "source": source,
        "amount": amount,
        "note": note
    }
    append_json("data/income.json", entry)

def log_strategy():
    method = input("Strategy used: ")
    result = input("Successful? (yes/no): ")
    comment = input("Reflection: ")
    entry = {
        "date": str(datetime.now()),
        "method": method,
        "result": result,
        "comment": comment
    }
    append_json("data/strategy.json", entry)

def log_donation():
    source = input("Donor/platform: ")
    amount = input("Amount offered/requested: ")
    status = input("Status (pending/received/rejected): ")
    entry = {
        "date": str(datetime.now()),
        "source": source,
        "amount": amount,
        "status": status
    }
    append_json("data/donation.json", entry)

def append_json(filename, data):
    with open(filename, "r+") as f:
        try:
            records = json.load(f)
        except:
            records = []
        records.append(data)
        f.seek(0)
        json.dump(records, f, indent=2)
    print("✅ Entry saved successfully.")
