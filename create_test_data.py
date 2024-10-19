import pandas as pd

# Sample employee data for test_employees.csv
test_employees_data = {
    "Employee_Name": ["Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince"],
    "Employee_EmailID": [
        "alice.johnson@acme.com",
        "bob.smith@acme.com",
        "charlie.brown@acme.com",
        "diana.prince@acme.com",
    ],
}

# Sample previous Secret Santa assignments for test_previous_santa.csv
test_previous_santa_data = {
    "Employee_Name": ["Alice Johnson", "Bob Smith"],
    "Employee_EmailID": ["alice.johnson@acme.com", "bob.smith@acme.com"],
    "Secret_Child_Name": ["Charlie Brown", "Diana Prince"],
    "Secret_Child_EmailID": ["charlie.brown@acme.com", "diana.prince@acme.com"],
}

# Convert the dictionaries into DataFrames
test_employees_df = pd.DataFrame(test_employees_data)
test_previous_santa_df = pd.DataFrame(test_previous_santa_data)

# File paths for saving
test_employees_path = "test_employees.csv"
test_previous_santa_path = "test_previous_santa.csv"

# Save DataFrames to CSV
test_employees_df.to_csv(test_employees_path, index=False)
test_previous_santa_df.to_csv(test_previous_santa_path, index=False)

(test_employees_path, test_previous_santa_path)
