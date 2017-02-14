from unittest import TestCase
from variable import DdExpression


class TestDdExpression(TestCase):

    def test_create_variable(self):
        var = DdExpression('A')
        self.assertEqual(var.dd_id, ('A',))

    def test_add_variable(self):
        var_a = DdExpression('A')
        var_b = DdExpression('B')
        sum_expr = var_a + var_b
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), 7)
        sum_expr = var_a + 2
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), 5)
        sum_expr = 2 + var_b
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), 6)

    def test_sub_variable(self):
        var_a = DdExpression('A')
        var_b = DdExpression('B')
        sum_expr = var_a - var_b
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), -1)
        sum_expr = var_b - 1
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), 3)
        sum_expr = 1 - var_a
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), -2)

    def test_mult_variable(self):
        var_a = DdExpression('A')
        var_b = DdExpression('B')
        sum_expr = var_a * var_b
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), 12)
        sum_expr = var_a * 10
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), 30)
        sum_expr = 10 * var_b
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), 40)

    def test_div_variable(self):
        var_a = DdExpression('A')
        var_b = DdExpression('B')
        sum_expr = var_a / var_b
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 2}), 1.5)
        sum_expr = var_a / 10
        self.assertEqual(sum_expr.evaluate({'A': 3, 'B': 4}), 0.3)

    def test_complex(self):
        var_a = DdExpression('A')
        var_b = DdExpression('B')
        var_c = DdExpression('C')
        var_d = DdExpression('D')
        sum_expr = 4*var_a + var_b - var_c * var_d
        self.assertEqual(sum_expr.evaluate({'A': 1, 'B': 2, 'C': 3, 'D': 4}), -6)
        sum_expr = 4*var_a + 3*(var_b - var_c * (2 - var_d))
        self.assertEqual(sum_expr.evaluate({'A': 1, 'B': 2, 'C': 3, 'D': 4}), 28)
        self.assertEqual(sum_expr.expression_repr, "((A)*(4))+(((B)-((C)*(((D)-(2))*(-1))))*(3))")

    def test_equalities(self):
        var_a = DdExpression('A')
        var_b = DdExpression('B')
        var_c = DdExpression('C')
        var_d = DdExpression('D')
        sum_expr = var_a < var_b
        self.assertEqual(sum_expr.evaluate({'A': 1, 'B': 2}), True)
        sum_expr = var_a < -1
        self.assertEqual(sum_expr.evaluate({'A': 1, 'B': 2}), False)
        sum_expr = 0 < var_b
        self.assertEqual(sum_expr.evaluate({'A': 1, 'B': 2}), True)
        sum_expr = var_a == 1
        self.assertEqual(sum_expr.evaluate({'A': 1, 'B': 2}), True)
        sum_expr = var_a <= 1
        self.assertEqual(sum_expr.evaluate({'A': 1, 'B': 2}), True)
        sum_expr = (4*var_a + var_b) < (var_c * var_d)
        self.assertEqual(sum_expr.evaluate({'A': 1, 'B': 2, 'C': 3, 'D': 4}), True)
        sum_expr = (4*var_a + var_b) < (var_c * var_d - 20)
        self.assertEqual(sum_expr.evaluate({'A': 1, 'B': 2, 'C': 3, 'D': 4}), False)
