import unittest
from calorie_calculator import calculate_bmr, calculate_tdee

class TestCalorieCalculations(unittest.TestCase):

    def test_calculate_bmr_male(self):
        # Mifflin-St Jeor: (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) + 5
        # (10 * 70) + (6.25 * 170) - (5 * 30) + 5
        # 700 + 1062.5 - 150 + 5 = 1617.5
        self.assertAlmostEqual(calculate_bmr(weight_kg=70, height_cm=170, age_years=30, gender='male'), 1617.5)

    def test_calculate_bmr_female(self):
        # Mifflin-St Jeor: (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) - 161
        # (10 * 60) + (6.25 * 160) - (5 * 25) - 161
        # 600 + 1000 - 125 - 161 = 1314
        self.assertAlmostEqual(calculate_bmr(weight_kg=60, height_cm=160, age_years=25, gender='female'), 1314.0)

    def test_calculate_bmr_invalid_gender(self):
        with self.assertRaises(ValueError):
            calculate_bmr(weight_kg=70, height_cm=170, age_years=30, gender='other')

    def test_calculate_tdee_sedentary(self):
        bmr = 1500
        # 1500 * 1.2 = 1800
        self.assertAlmostEqual(calculate_tdee(bmr, 'sedentary'), 1800.0)
        self.assertAlmostEqual(calculate_tdee(bmr, 'Sedentary'), 1800.0) # Test case insensitivity
        self.assertAlmostEqual(calculate_tdee(bmr, '  sedentary  '), 1800.0) # Test stripping of whitespace


    def test_calculate_tdee_moderately_active(self):
        bmr = 1600
        # 1600 * 1.55 = 2480
        self.assertAlmostEqual(calculate_tdee(bmr, 'moderately active'), 2480.0)
        self.assertAlmostEqual(calculate_tdee(bmr, 'MODERATELY ACTIVE'), 2480.0) # Test case insensitivity

    def test_calculate_tdee_invalid_activity(self):
        bmr = 1500
        with self.assertRaises(ValueError):
            calculate_tdee(bmr, 'hyper active')
        with self.assertRaises(ValueError):
            calculate_tdee(bmr, '') # Test empty string

if __name__ == '__main__':
    unittest.main()
