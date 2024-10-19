import unittest
from secret_santa import SecretSanta, Employee


class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        """Set up test with sample data."""
        self.santa = SecretSanta("test_employees.csv", "test_previous_santa.csv")

    def test_employee_list(self):
        """Test if employees are read correctly."""
        employees = self.santa.employees
        self.assertEqual(len(employees), 4)  # Check the number of employees
        self.assertEqual(employees[0].name, "Alice Johnson")  # Compare full name

    def test_generate_secret_santa(self):
        """Test that Secret Santa assignments are valid."""
        assignments = self.santa.generate_secret_santa()
        self.assertEqual(
            len(assignments), len(self.santa.employees)
        )  # All employees should have assignments

        # Ensure no one is their own Secret Santa
        for giver, recipient in assignments.items():
            self.assertNotEqual(giver.email, recipient.email)

    def test_previous_assignments(self):
        """Test that previous year assignments are respected."""
        assignments = self.santa.generate_secret_santa()
        for giver, recipient in assignments.items():
            if giver.email in self.santa.previous_assignments:
                self.assertNotEqual(
                    self.santa.previous_assignments[giver.email], recipient.email
                )


if __name__ == "__main__":
    unittest.main()
