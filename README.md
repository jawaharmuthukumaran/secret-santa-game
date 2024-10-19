Here's a polished and structured `README.md` for your project.

---

# Secret Santa Game

## Project Description

This project automates the assignment of Secret Santa pairs for a company event, ensuring the following constraints:

1. An employee cannot be assigned to themselves.
2. An employee cannot have the same secret child as in the previous year.
3. Each employee must be assigned one and only one secret child.
4. The program outputs a CSV file with the new Secret Santa pairings.

## Installation

1. **Clone the Repository:**
   - If you have access to the Git repository, use:
     ```bash
     git clone <repository-url>
     cd secret_santa_game
     ```

## Usage

1. **Prepare Input Files:**

   - **`employees.csv`:** Contains employee details with headers: `Employee_Name`, `Employee_EmailID`.
   - **`previous_santa.csv`:** Contains last year’s Secret Santa assignments with headers: `Employee_Name`, `Employee_EmailID`, `Secret_Child_Name`, `Secret_Child_EmailID`.

2. **Run the Secret Santa Program:**

   - Navigate to the `secret_santa_game` directory and execute:
     ```bash
     python secret_santa.py
     ```

3. **Output:**

   - The program will generate a new CSV file called `secret_santa_assignments.csv` with the following columns:
     - `Employee_Name`
     - `Employee_EmailID`
     - `Secret_Child_Name`
     - `Secret_Child_EmailID`

4. **Example:**
   - You can modify the input files (`employees.csv`, `previous_santa.csv`) to test different scenarios.
   - Make sure the files are present in the `secret_santa_game` directory before running the program.

## Testing

1. **Run Unit Tests:**

   - Ensure you are in the `secret_santa_game` directory and run:
     ```bash
     python test_secret_santa.py
     ```
   - The tests validate the assignment logic and ensure it meets the constraints.

2. **Testing with New Data:**
   - Modify the test files (`test_employees.csv`, `test_previous_santa.csv`) or create new ones to validate different scenarios.

## Error Handling

The program includes error handling for:

1. **File Not Found:**
   - If an input file (`employees.csv` or `previous_santa.csv`) is missing, an error message will be displayed.
2. **Invalid File Format:**
   - If the input files do not match the expected CSV format, the program raises an error.
3. **Assignment Constraints:**
   - If the constraints cannot be satisfied (e.g., no valid child available for an employee), an error is raised, indicating the need to adjust the input data.

## Extensibility

The project is designed to be easily extendable:

1. **New Constraints:**
   - Additional constraints can be integrated into the logic in `secret_santa.py`.
2. **Modularity:**
   - The code is modular, allowing for easy updates, additions, or modifications to the assignment logic.
3. **Custom Output Formats:**
   - You can modify the output CSV structure to include additional fields or generate other formats (e.g., JSON).

## Version Control

Use Git for version control:

1. **Initialize a Git repository (if not already done):**

   ```bash
   git init
   ```

2. **Add changes to the repository:**

   ```bash
   git add .
   ```

3. **Commit changes:**

   ```bash
   git commit -m "Add Secret Santa assignment logic"
   ```

4. **Push to remote repository:**
   ```bash
   git remote add origin <repository-url>
   git push -u origin main
   ```
