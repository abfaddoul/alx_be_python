import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """تحضير الكالكولاتور قبل كل اختبار"""
        self.calc = SimpleCalculator()

    # -----------------------------
    # ✅ اختبارات الجمع (Addition)
    # -----------------------------
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertEqual(self.calc.add(-2.5, -2.5), -5.0)

    # -----------------------------
    # ✅ اختبارات الطرح (Subtraction)
    # -----------------------------
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
        self.assertEqual(self.calc.subtract(2.5, 1.0), 1.5)
        self.assertEqual(self.calc.subtract(-5, 5), -10)

    # -----------------------------
    # ✅ اختبارات الضرب (Multiplication)
    # -----------------------------
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(-1.5, -2), 3.0)

    # -----------------------------
    # ✅ اختبارات القسمة (Division)
    # -----------------------------
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(-9, -3), 3)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))  # Optional case

# 🏁 لتشغيل الاختبارات من هذا الملف مباشرة
if __name__ == '__main__':
    unittest.main()
