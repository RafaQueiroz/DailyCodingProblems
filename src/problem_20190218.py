from datetime import datetime


class Clock:
    DEGREES_PER_MINUTE = 0.5

    def __init__(self, text_hour):
        if not self._its_valid_hour(text_hour):
            raise ClockException(
                "{0} it's not a valid hour. Please provide something between 00:00 and 24:00.".format(text_hour))

        self.hours, self.minutes = self._separate_time(text_hour)

    def nearest_hands_angle(self):

        hour_hand_position = self._degree_hour_hand_position() + self._hour_hand_position_correction()

        result_angle = hour_hand_position - self._degree_minute_hand_position()

        if result_angle > 180:
            return self._complementary_angle(result_angle)

        return result_angle

    def _hour_hand_position_correction(self):
        return Clock.DEGREES_PER_MINUTE * self.minutes

    def _degree_hour_hand_position(self):
        return (self.hours * 360) / 12

    def _degree_minute_hand_position(self):
        return (self.minutes * 360) / 60

    def _complementary_angle(self, angle):
        return 360 - angle

    def _its_valid_hour(self, text_hour):
        try:
            datetime.strptime(text_hour, '%H:%M')
            return True
        except Exception:
            return False

    def _separate_time(self, text_hour):
        return [int(part) for part in text_hour.split(':')]


class ClockException(Exception):
    pass
