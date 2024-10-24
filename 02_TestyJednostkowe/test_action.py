import unittest
import action  # import py file


# tworze klase i tworze unitest
class TestAction(unittest.TestCase):
    def test_NWD(self):  # argumentem jest self test_
        self.assertEqual(action.NWD(28, 12), 4)  # sprawdzam czy wynik jest to co chce
        self.assertEqual(action.NWD(30, 7), 1)
        self.assertEqual(action.NWD(30, 3), 3)

if __name__ == '__main__':
    unittest.main() # sprawia, że jeśli uruchomisz plik bezpośrednio, testy zostaną wykonane.

# w shell piszę --> python -m unittest test_action.py
