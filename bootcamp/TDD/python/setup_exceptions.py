from bootcamp.TDD.python.clac import Calculator


def setUp(self):
    self.calculator = Calculator()


def test_sum(self):
    result = self.calculator.sum(1, 2)
    self.assertEqual(result, 3)


def test_divide_happy_path(self):
    result = self.calculator.divide(4, 2)
    self.assertEqual(result, 2)

    result = self.calculator.divide(2, 4)
    self.assertEqual(result, 0.5)  # oops for py2


def test_divide_by_zero(self):
    self.assertRaises(ZeroDivisionError, lambda: self.calculator.divide(4, 0))
