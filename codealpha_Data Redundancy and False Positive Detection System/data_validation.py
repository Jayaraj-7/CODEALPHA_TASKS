import pandas as pd
import os

DATABASE_FILE = "database.csv"

# Create database if not exists
if not os.path.exists(DATABASE_FILE):
    df = pd.DataFrame(columns=["ID", "Name", "Email"])
    df.to_csv(DATABASE_FILE, index=False)

def validate_and_add(new_record):
    df = pd.read_csv(DATABASE_FILE)

    # Check duplicate ID
    if new_record["ID"] in df["ID"].values:
        print("❌ Duplicate ID detected. Record rejected.")
        return

    # Check duplicate Email
    if new_record["Email"] in df["Email"].values:
        print("❌ Duplicate Email detected. Record rejected.")
        return

    # Add unique record
    df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    df.to_csv(DATABASE_FILE, index=False)

    print("✅ Unique and verified data added successfully.")

# Sample records
record1 = {
    "ID": 101,
    "Name": "John",
    "Email": "john@gmail.com"
}

record2 = {
    "ID": 101,
    "Name": "John Smith",
    "Email": "johnsmith@gmail.com"
}

validate_and_add(record1)
validate_and_add(record2)