import csv
import random
from typing import List, Dict


class Employee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class SecretSanta:
    def __init__(self, employees_file: str, previous_santa_file: str = None):
        self.employees = self.read_employees(employees_file)
        self.previous_assignments = (
            self.read_previous_assignments(previous_santa_file)
            if previous_santa_file
            else {}
        )

    def read_employees(self, filename: str) -> List[Employee]:
        """Reads employee information from CSV."""
        employees = []
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employees.append(
                        Employee(row["Employee_Name"], row["Employee_EmailID"])
                    )
        except FileNotFoundError:
            raise Exception(f"File {filename} not found.")
        return employees

    def read_previous_assignments(self, filename: str) -> Dict[str, str]:
        """Reads the previous Secret Santa assignments from CSV and returns a dictionary."""
        previous_assignments = {}
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    previous_assignments[row["Employee_EmailID"]] = row[
                        "Secret_Child_EmailID"
                    ]
        except FileNotFoundError:
            return {}  # No previous assignments
        return previous_assignments

    def generate_secret_santa(self) -> Dict[Employee, Employee]:
        """Generates Secret Santa assignments ensuring no employee is assigned to themselves."""
        remaining = self.employees[:]
        secret_santa_map = {}

        for giver in self.employees:
            possible_recipients = [
                e
                for e in remaining
                if e.email != giver.email
                and (
                    giver.email not in self.previous_assignments
                    or self.previous_assignments[giver.email] != e.email
                )
            ]

            if not possible_recipients:
                raise Exception(
                    f"Cannot find valid assignment for {giver.name}. Retry shuffling."
                )

            recipient = random.choice(possible_recipients)
            secret_santa_map[giver] = recipient
            remaining.remove(recipient)

        return secret_santa_map

    def save_assignments(self, output_file: str, assignments: Dict[Employee, Employee]):
        """Writes the Secret Santa assignments to a CSV file."""
        with open(output_file, mode="w", newline="") as file:
            fieldnames = [
                "Employee_Name",
                "Employee_EmailID",
                "Secret_Child_Name",
                "Secret_Child_EmailID",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for giver, recipient in assignments.items():
                writer.writerow(
                    {
                        "Employee_Name": giver.name,
                        "Employee_EmailID": giver.email,
                        "Secret_Child_Name": recipient.name,
                        "Secret_Child_EmailID": recipient.email,
                    }
                )


if __name__ == "__main__":
    santa = SecretSanta("employees.csv", "previous_santa.csv")
    assignments = santa.generate_secret_santa()
    santa.save_assignments("secret_santa_assignments.csv", assignments)
