from bootcamp.TDD.python.clac import Calculator


def test_sum(self):
    calculator = Calculator()  # arrange
    result = calculator.sum(1, 2)  # act
    self.assertEqual(result, 3)  # assert
