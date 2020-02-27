import unittest

from parameterized import parameterized

from src.problem_20190218 import Clock, ClockException


class NearestAngleTest(unittest.TestCase):
    '''
     Good morning! Here's your coding interview problem for today.
    This problem was asked by Microsoft.
    Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

    Bonus: When, during the course of a day, will the angle be zero?
    '''

    def test_wrong_hour_format(self):
        with self.assertRaises(ClockException) as e:
            Clock("99:00")

        self.assertEqual("99:00 it's not a valid hour. Please provide something between 00:00 and 24:00.",
                         e.exception.args[0])

    def test_right_time_format(self):
        self.assertIsNotNone(Clock("09:59"))

    def test_2359_hours_is_valid(self):
        self.assertIsNotNone(Clock("23:59"))

    @parameterized.expand([
        ("12:30", 165), ("12:40", 140), ("12:15", 82.5), ("12:00", 0)
    ])
    def test_has_correct_angle(self, text_hour, result_angle):
        clock = Clock(text_hour)
        self.assertEqual(result_angle, clock.nearest_hands_angle())


if __name__ == "__main__":
    unittest.main()
