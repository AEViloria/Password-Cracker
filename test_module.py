import unittest
from password_cracker import crack_password

class TestPasswordCracker(unittest.TestCase):
    def test_no_salts(self):
        self.assertEqual(crack_password("b305921a3723cd5d70a375cd21a61e60aabb84ec"), "sammy123")
        self.assertEqual(crack_password("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e"), "abacab")
        self.assertEqual(crack_password("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"), "password")

    def test_with_salts(self):
        self.assertEqual(crack_password("53d8b3dc9d39f0184144674e310185e41a87ffd5", True), "superman")
        self.assertEqual(crack_password("da5a4e8cf89539e66097acd2f8af128acae2f8ae", True), "q1w2e3r4t5")
        self.assertEqual(crack_password("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", True), "bubbles1")

if __name__ == "__main__":
    unittest.main()
